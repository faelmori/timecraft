# TimeCraft Banner
![TimeCraft Banner](docs/assets/top_banner.png)

---

**An advanced solution for time series analysis, database integration, and task automation, with dynamic notifications and a powerful CLI.**

---

## **Table of Contents**
1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
    - [CLI](#cli)
    - [Examples](#examples)
    - [Configuration](#configuration)
5. [Scheduled Execution](#scheduled-execution)
6. [Webhook Notifications](#webhook-notifications)
7. [Roadmap](#roadmap)
8. [Contributing](#contributing)
9. [Contact](#contact)

---

## **About the Project**
TimeCraft is a flexible and powerful solution for time series analysis, database integration, and task automation. Developed in **Python**, it offers webhook notification support, scheduled model execution, and an intuitive CLI to streamline data workflows.

**Why TimeCraft?**
- 📈 **Advanced Analysis**: Robust scripts for modeling, forecasting, and evaluating temporal data.
- 🛢️ **Simple Integration**: Tools to connect and query multiple database systems.
- ⚙️ **Automation & Notifications**: Modules to automate data workflows and send alerts.

---

## **Features**
✨ **Plug-and-Play Models**:
- ARIMA, Prophet, LSTM, and other ready-to-use models.
- Easy customization and extension.

🔗 **Database Integration**:
- Efficient connection to different database systems.
- Scripts for data import and querying.

⏰ **Scheduled Execution**:
- Schedule automatic model runs (cronjob-like).
- CLI and Python API for scheduling.

🔔 **Dynamic Notifications**:
- Send notifications via Webhook (Slack, Discord, custom APIs).
- Customizable payloads for each platform.

💻 **Powerful CLI**:
- Simple commands to run models, schedule executions, and monitor tasks.
- Extensible for new workflows.

---

## **Installation**
Requirements:
- **Python** 3.8 or higher.

```bash
# Clone the repository
git clone https://github.com/rafa-mori/timecraft.git
cd timecraft

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## **Usage**

### CLI
Example commands with the TimeCraft CLI:

```bash
# Run TimeCraft model
python -m timecraft_ai run --data data/hist_cambio_float.csv --date_column dt --value_columns purchaseValue,saleValue --is_csv

# Schedule automatic execution (every 10 minutes)
python -m timecraft_ai schedule 600 timecraft
```

### **Python Usage Examples**

```python
from timecraft_ai import TimeCraftAI

tc = TimeCraftAI()
model = tc.create_timecraft_model(
    data="data/hist_cambio_float.csv",
    date_column="dt",
    value_columns=["purchaseValue", "saleValue"],
    is_csv=True
)
model.run()
```

#### **Scheduled Execution in Python**

```python
from timecraft_ai import run_scheduled
run_scheduled(model.run, interval_seconds=600)  # Runs every 10 minutes
```

---

### **Command and Flag Descriptions**
- **`--data`**: Path to the data file.
- **`--date_column`**: Name of the date column.
- **`--value_columns`**: Value columns to analyze.
- **`--is_csv`**: Indicates if the file is CSV.
- **`--model`**: Model type (`timecraft`, `classifier`, `regression`).

---

### **Configuration**
TimeCraft can be configured via command-line arguments or directly in Python code. For advanced configurations, see the examples in the `/tutorials` folder.

---

## **Scheduled Execution**
TimeCraft allows you to schedule automatic model runs, similar to a cronjob.

**Via CLI:**

```bash
python -m timecraft_ai schedule <interval_seconds> <model>
```

- `<interval_seconds>`: interval between executions (e.g., 600 for 10 minutes)
- `<model>`: model type (`timecraft`, `classifier`, `regression`)

**Via Python:**

```python
from timecraft_ai import run_scheduled
run_scheduled(model.run, interval_seconds=600)
```

> The scheduler runs in the background and can be stopped with Ctrl+C.

---

## **Webhook Notifications**
TimeCraft supports sending notifications to webhooks after model runs or analyses. Ideal for automation, monitoring, or integration with other systems (Slack, Discord, custom APIs).

### How it works
- Pass the `webhook_url` parameter to the `run` or `run_analysis` methods.
- When finished, a POST with a JSON payload is sent to the URL.
- Extra fields can be added via `webhook_payload_extra`.

**Example:**

```python
model.run(webhook_url="https://your-webhook.com/webhook")
```

**With extra payload:**

```python
model.run(
    webhook_url="https://your-webhook.com/webhook",
    webhook_payload_extra={"user": "rafa", "run_type": "nightly"}
)
```

**Slack:**

```python
model.run(
    webhook_url="https://hooks.slack.com/services/XXX/YYY/ZZZ",
    webhook_payload_extra={"text": "TimeCraft finished!"}
)
```

**Discord:**

```python
model.run(
    webhook_url="https://discord.com/api/webhooks/XXX/YYY",
    webhook_payload_extra={"content": "TimeCraft finished!"}
)
```

> The payload can be customized for each platform using `webhook_payload_extra`.

---

## **Roadmap**
🔜 **Upcoming Features**:
- Support for cloud data sources (BigQuery, Snowflake)
- Email notification system
- Dashboard for result visualization

---

## **Contributing**
Contributions are welcome! See the [Contributing Guide](CONTRIBUTING.md) for details.

---

## **Contact**
💌 **Developer**:  
[Rafael Mori](mailto:faelmori@gmail.com)
💼 [faelmori/timecraft on GitHub](https://github.com/rafa-mori/timecraft)
[LinkedIn: Rafa Mori](https://www.linkedin.com/in/rafa-mori)