
# AI-Powered Smart Home System (IoT with AI — Week 4 Major Capstone)

A complete AI-driven Smart Home Platform integrating multi-sensor telemetry (ESP32 with DHT11, PIR, LDR, and Sound sensors), TinyML models for occupancy prediction and energy optimization, AES-256 encrypted MQTT payload transmission, voice control parsing, and an interactive Streamlit dashboard[cite: 21].

---

## 📌 Architecture & Features

- **Multi-Sensor Array:** Temperature, Motion, Light, and Sound monitoring[cite: 21].
- **AI Analytics Engine:**
  - **Occupancy Prediction:** Random Forest Classifier estimating room occupancy[cite: 21].
  - **Energy Optimization:** Ridge Regression model dynamically optimizing HVAC and lighting loads[cite: 21].
- **Security Layer:** AES-256 Fernet symmetric payload encryption over MQTT[cite: 21].
- **Voice Control & Dashboard:** Streamlit UI supporting natural language voice command parsing and real-time metric tracking[cite: 21].
- **DevOps:** Fully containerized (`Dockerfile`) with automated GitHub Actions CI/CD workflows (`ci-cd.yml`)[cite: 21].

---



## 📁 Repository Structure

**Plaintext**

```
iot_week4_capstone_smarthome/
├── train_ai_models.py         # AI occupancy & energy model training script
├── mqtt_security.py           # AES-256 payload encryption module
├── esp32_sensors.ino          # ESP32 C++ firmware code
├── app.py                     # Streamlit smart home dashboard UI
├── Dockerfile                 # Docker container configuration
├── requirements.txt           # Dependencies
├── .github/workflows/
│   └── ci-cd.yml              # GitHub Actions CI/CD pipeline
└── README.md                  # Project documentation
```


## 🚀 How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
