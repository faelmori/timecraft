# ⏳ TimeCraft

Welcome to **TimeCraft**! This project was created to simplify time series analysis, database integration, and task automation.

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) ![Last Commit](https://img.shields.io/github/last-commit/faelmori/timecraft) ![Repo Size](https://img.shields.io/github/repo-size/faelmori/timecraft)

---

## 🚀 Key Features

* 📈 **Time Series Analysis**
  Robust scripts for modeling, forecasting, and evaluating temporal data.

* 🛢️ **Database Integration**
  Tools to efficiently connect to and query various database systems.

* ⚙️ **Automation & Notifications**
  Modules to automate data workflows and send notifications or alerts.

---

## 📁 Project Structure

```
timecraft/
├── /src/                # Core logic and modules
├── /docs/               # Documentation files (README, INSTALL, CONTRIBUTING)
├── /tutorials/          # Step-by-step guides and advanced use cases
├── /data/               # Sample datasets and generated results
├── /assets/             # Visual content for outreach and publications
├── /venv/               # Virtual environment and dependency management
└── requirements.txt     # Python dependencies
```

---

## 🧭 Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rafa-mori/timecraft.git
   cd timecraft
   ```

2. **Create and activate a virtual environment** *(optional but recommended)*:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Explore the tutorials**:
   Navigate to the `/tutorials` folder for usage examples and best practices.

---

## 📚 Tutorials & Examples

| Topic                                               | Description                                                  |
| --------------------------------------------------- | ------------------------------------------------------------ |
| [Time Series Forecasting](tutorials/forecasting.md) | Learn how to model and predict future data points.           |
| [Database Connection](tutorials/database.md)        | Connect to and retrieve data from supported databases.       |
| [Automation Pipeline](tutorials/automation.md)      | Build and schedule tasks using TimeCraft’s automation tools. |

---

## 🗣️ MCP Voice & Chatbot Server (Nova Feature)

O TimeCraft agora conta com um servidor MCP (Multi-Command Processor) com chatbot embutido, pronto para comandos por voz e texto, análise de dados, insights e integração opcional com LLMs/plugins externos!

### Principais Endpoints (FastAPI)

- **/health** — Health check do servidor
- **/mcp/command** — Envie comandos de texto para o MCP (chatbot)
- **/mcp/plugins** — Liste, ative/desative e configure plugins/LLMs (ex: OpenAI)

#### Exemplos de uso

```bash
# Health check
curl http://localhost:8000/health

# Enviar comando para o chatbot
curl -X POST http://localhost:8000/mcp/command -H "Content-Type: application/json" -d '{"message": "me mostre o histórico"}'

# Listar plugins/LLMs
curl http://localhost:8000/mcp/plugins

# Ativar plugin OpenAI
curl -X POST http://localhost:8000/mcp/plugins/openai/enable

# Configurar chave de API do OpenAI
curl -X POST http://localhost:8000/mcp/plugins/openai/config -H "Content-Type: application/json" -d '{"api_key": "SUA_CHAVE_AQUI"}'
```

### Como rodar o servidor

```bash
uvicorn src.timecraft_ai.mcp_server:app --reload
```

### Recursos do MCP
- Processamento de comandos por voz (Vosk + Porcupine)
- Síntese de voz (pyttsx3)
- Chatbot integrado com análise de dados, previsão e insights
- Modular: plugins/LLMs ativados só se configurados
- Baixo custo computacional e monetário por padrão

Veja o código-fonte em [`src/timecraft_ai/`](./timecraft_ai/) para detalhes e exemplos de integração.

---

## 🗣️ Como usar o MCP por voz

O TimeCraft permite interação totalmente hands free via comandos de voz, com ativação por hotword e resposta falada!

### Pré-requisitos
- Microfone conectado ao computador
- Dependências instaladas: `vosk`, `pyaudio`, `pyttsx3`, `pvporcupine`
- (Opcional) Configurar o modelo Vosk para o idioma desejado (exemplo: `models/vosk-model-small-pt`)

### Como rodar o processador de áudio

```bash
python -m timecraft_ai.audio_processor
```

Ou diretamente pelo arquivo:

```bash
python src/timecraft_ai/audio_processor.py
```

### Funcionamento
- O sistema aguarda a palavra-chave (hotword), por padrão: `mcp`
- Após detectar a hotword, grava e transcreve seu comando
- O comando é processado pelo MCP e a resposta é falada de volta

#### Exemplo de fluxo
1. Diga: **"MCP"** (aguarde a confirmação)
2. Fale: **"Me mostre o histórico"**
3. O MCP responde em voz: "Esses são os dados históricos: ..."

Você pode customizar a hotword, voz e outros parâmetros editando o arquivo `audio_processor.py`.

---

## 🤝 Contributing

Contributions of all kinds are welcome!
Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to help improve TimeCraft.

---

## 🛣️ Planned Features (Roadmap)

* ✅ Plug-and-play models for ARIMA, Prophet, and LSTM
* 🚧 Support for cloud-based data sources (e.g., BigQuery, Snowflake)
* 🔔 Email and webhook notification system
* 📊 Dashboard interface for visual result presentation (optional module)

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


## 📧 Contact

If you have any questions or feedback, please feel free to reach out:

- Email: [faelmori@gmail.com](mailto:faelmori@gmail.com)
- GitHub: [faelmori/timecraft](https://github.com/rafa-mori/timecraft)
- LinkedIn: [Rafa Mori](https://www.linkedin.com/in/rafa-mori)

---

