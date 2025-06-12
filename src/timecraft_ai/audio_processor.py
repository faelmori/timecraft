import sys
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer
from .mcp_command_handler import MCPCommandHandler
from .voice_synthesizer import VoiceSynthesizer
from .hotword_detector import HotwordDetector

class AudioProcessor:
    def __init__(self, model_path: str = "models/vosk-model-small-pt", rate: int = 16000, chunk: int = 8192, command_handler=None, voice_synthesizer=None, hotword_detector=None):
        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, rate)
        self.rec.SetWords(True)
        self.rate = rate
        self.chunk = chunk
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)
        self.command_handler = command_handler
        self.voice_synthesizer = voice_synthesizer
        self.hotword_detector = hotword_detector

    def listen_and_transcribe(self):
        print("🎤 Capturando áudio... Fale algo!")
        try:
            while True:
                data = self.stream.read(self.chunk)
                if self.rec.AcceptWaveform(data):
                    result = json.loads(self.rec.Result())
                    text = result["text"]
                    print("📝 Transcrição:", text)
                    if self.command_handler and text.strip():
                        response = self.command_handler.handle(text)
                        print("🤖 Resposta:", response)
                        if self.voice_synthesizer:
                            self.voice_synthesizer.speak(response)
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário.")
        finally:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

    def listen_and_transcribe_once(self):
        """Captura e transcreve um único comando de voz."""
        print("🎤 Fale seu comando...")
        data = self.stream.read(self.chunk)
        if self.rec.AcceptWaveform(data):
            result = json.loads(self.rec.Result())
            text = result["text"]
            print("📝 Transcrição:", text)
            if self.command_handler and text.strip():
                response = self.command_handler.handle(text)
                print("🤖 Resposta:", response)
                if self.voice_synthesizer:
                    self.voice_synthesizer.speak(response)

    def run_with_hotword(self):
        print("MCP pronto para comandos por voz!")
        try:
            while True:
                if self.hotword_detector:
                    self.hotword_detector.listen_for_hotword()
                self.listen_and_transcribe_once()
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário.")
        finally:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

if __name__ == "__main__":
    handler = MCPCommandHandler()
    synthesizer = VoiceSynthesizer()
    hotword = HotwordDetector(keyword="mcp")
    processor = AudioProcessor(command_handler=handler, voice_synthesizer=synthesizer, hotword_detector=hotword)
    processor.run_with_hotword()
