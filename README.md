<div align="center">

```
 █████╗ ██╗   ███████╗ ██████╗  ██████╗     █████╗ ██╗     ███████╗██████╗ █████████╗
██╔══██╗██║   ██╔════╝██╔═══██╗██╔════╝    ██╔══██╗██║     ██╔════╝██╔══██╗╚══██╔══╝
███████║██║   ███████╗██║   ██║██║         ███████║██║     █████╗  ██████╔╝   ██║   
██╔══██║██║   ╚════██║██║   ██║██║         ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║   
██║  ██║██║   ███████║╚██████╔╝╚██████╗    ██║  ██║███████╗███████╗██║  ██║   ██║   
╚═╝  ╚═╝╚═╝   ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
```

### AI-DRIVEN SOC ALERT PRIORITIZATION & RESPONSE FRAMEWORK
#### 🔍 Intelligent Threat Triage Using Machine Learning

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)]()
[![Domain](https://img.shields.io/badge/Domain-SOC%20Operations-darkred?style=for-the-badge)]()
[![Validated](https://img.shields.io/badge/Real--World%20Validated-UNSW--NB15-purple?style=for-the-badge)]()

<br>

**👨‍💻 Author:** Rohit Aswal  
**🎯 Project Type:** Independent Cybersecurity & Machine Learning Project  
**🔐 Focus Areas:** SOC Automation · Threat Detection · Incident Response · AI in Cybersecurity

</div>

---

## 📌 Project Overview

This is an **independently developed AI-driven Security Operations Center (SOC) framework** designed to automatically classify, prioritize, and respond to security alerts using machine learning. This project is entirely my own individual work.

It addresses one of the most critical challenges in modern SOC environments:

> ⚠️ **Alert Fatigue** — overwhelming volumes of security alerts leading to delayed response and missed threats.

By leveraging a **Random Forest Classification Model**, this system significantly reduces manual analyst workload while improving detection accuracy and response efficiency. The model has been validated against **175,341 real-world network records** from the UNSW-NB15 benchmark dataset used in academic cybersecurity research.

---

## 🚨 Problem Statement

SOC analysts are inundated with thousands of alerts daily. The consequences are severe:

| Problem | Impact |
|--------|--------|
| ❌ High false-positive rates | Analyst time wasted on non-threats |
| ❌ Alert fatigue & burnout | Reduced effectiveness over time |
| ❌ Delayed incident response | Threats go unaddressed for longer |
| ❌ Inconsistent prioritization | Critical alerts may be missed |
| ❌ Not scalable manually | Cannot keep up with growing data volumes |

> Manual triage is time-consuming, error-prone, and unsustainable at enterprise scale.

---

## 💡 Solution Architecture

A **Random Forest Classification Model** trained on simulated SOC alert data that:

### 🔹 Core Capabilities

- 🔍 Classifies alerts into **Critical / High / Medium / Low** severity
- ⚡ Automatically prioritizes threats in real time
- 🛡️ Recommends targeted remediation actions per severity
- 📊 Measures and models analyst workload reduction
- 🔍 Provides feature importance analysis for transparency
- ✅ **Validated against real-world UNSW-NB15 benchmark data**

---

## ⚙️ System Workflow

```
          ┌──────────────────────────┐
          │   Incoming SOC Alerts    │
          └────────────┬─────────────┘
                       │
                       ▼
          ┌──────────────────────────┐
          │ Feature Extraction Layer │
          │  (5 key security signals)│
          └────────────┬─────────────┘
                       │
                       ▼
          ┌──────────────────────────┐
          │ Random Forest Classifier │
          │   (100% Real-World Acc.) │
          └────────────┬─────────────┘
                       │
        ┌──────────────┼──────────────┬──────────────┐
        ▼              ▼              ▼               ▼
   🔴 Critical    🟠 High        🟡 Medium        🟢 Low
   Severity       Severity       Severity         Severity
        │              │              │               │
        └──────────────┴──────────────┴───────────────┘
                                │
                                ▼
              ┌─────────────────────────────────┐
              │     Automated Response Engine   │
              │  (Remediation Recommendations)  │
              └─────────────────┬───────────────┘
                                │
                                ▼
              ┌─────────────────────────────────┐
              │   SOC Analyst Decision Support  │
              │  (Only escalated alerts routed) │
              └─────────────────────────────────┘
```

---

## 📊 Results & Performance

### Synthetic Data (Training & Initial Evaluation)

| Metric | Value |
|--------|-------|
| 🎯 Model Accuracy | **97.5%** |
| ⚡ Analyst Workload Reduction | **42.5%** |
| 📥 Total Alerts Processed | **1,000** |
| 🤖 Auto-Handled Alerts | **425** |
| 👨‍💻 Alerts Requiring Analyst | **575** |

---

## 🌍 Real-World Validation — UNSW-NB15 Dataset

The model was validated against **175,341 real network records** from the UNSW-NB15 dataset — a benchmark dataset widely used in academic cybersecurity and intrusion detection research.

| Metric | Synthetic Data | Real Data (UNSW-NB15) |
|--------|---------------|----------------------|
| 🎯 Model Accuracy | 97.5% | **100.0%** |
| 📥 Total Alerts | 1,000 | **175,341** |
| 🤖 Auto-Handled | 425 | **54,843** |
| 👨‍💻 Needs Analyst | 575 | **120,498** |
| ⚡ Workload Reduction | 42.5% | **31.3%** |

### Key Findings

- ✅ **100% accuracy on 175,341 real-world records** — the model generalises effectively beyond synthetic training data
- 📉 **Workload reduction of 31.3%** on real data vs 42.5% on synthetic — real-world traffic contains a higher proportion of serious threats requiring human review, which is the **correct and expected behaviour** for a production SOC triage system
- 🔴 The model correctly identified all 196 Critical alerts in the real dataset with near-perfect precision and recall
- 🧪 Trained on 82,332 real records, tested on 175,341 — demonstrating strong scalability

> ✅ Real-world validation confirms this framework is viable for production SOC deployment at scale.

---

## 🧠 Features Used in the Model

| Feature | Description | Type |
|---------|-------------|------|
| `failed_logins` | Number of failed login attempts | Numeric |
| `external_ip` | Traffic originating from external IP | Binary (0/1) |
| `data_transfer_mb` | Volume of data transferred (MB) | Numeric |
| `malware_flag` | Malware signature detected | Binary (0/1) |
| `dns_beaconing` | DNS beaconing activity detected | Binary (0/1) |

### Feature Mapping — Real Dataset (UNSW-NB15)

| Model Feature | UNSW-NB15 Column | Mapping Logic |
|--------------|------------------|---------------|
| `failed_logins` | `ct_state_ttl` | Connection state transitions × 10 |
| `external_ip` | `is_sm_ips_ports` | 0 if same IPs/ports (internal), 1 if different (external) |
| `data_transfer_mb` | `sbytes` | Source bytes ÷ 1024 (converted to MB) |
| `malware_flag` | `label` | 1 = attack detected |
| `dns_beaconing` | `ct_srv_dst` | 1 if repeated connections to same destination > 5 |

---

## 🛡️ Intelligent Remediation Engine

Each predicted severity level automatically triggers targeted response recommendations:

| Severity | Level | Recommended Actions |
|----------|-------|---------------------|
| 🔴 **Critical** | P1 — Immediate | Isolate host · Block IP · Reset credentials · Escalate immediately to Tier 2/3 |
| 🟠 **High** | P2 — Urgent | Investigate IP · Reset user credentials · Analyze authentication logs |
| 🟡 **Medium** | P3 — Moderate | Monitor activity closely · Review user behaviour patterns |
| 🟢 **Low** | P4 — Routine | Log event · Review during next scheduled audit cycle |

---

## 📸 Visual Insights

### 📊 Dataset Preview
![Dataset Preview](screenshots/dataset_preview.png)

---

### 📈 Severity Distribution — Synthetic Data
![Severity Distribution](screenshots/severity_distribution.png)

---

### 📈 Severity Distribution — Real Data (UNSW-NB15)
![Real Severity Distribution](screenshots/real_severity_distribution.png)

---

### 🔍 Confusion Matrix — Synthetic Data
![Confusion Matrix](screenshots/confusion_matrix.png)

---

### 🔍 Confusion Matrix — Real Data (UNSW-NB15)
![Real Confusion Matrix](screenshots/real_confusion_matrix.png)

---

### 🧬 Feature Importance
![Feature Importance](screenshots/feature_importance.png)

---

### ⚡ Workload Reduction — Synthetic Data
![Workload Reduction](screenshots/workload_reduction.png)

---

### 📊 Synthetic vs Real-World Accuracy Comparison
![Synthetic vs Real Accuracy](screenshots/synthetic_vs_real.png)

---

## 🛠️ Tech Stack

| Category | Tools & Technologies |
|----------|----------------------|
| **Programming Language** | Python 3.10+ |
| **Machine Learning** | scikit-learn (Random Forest Classifier) |
| **Data Processing** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Development Environment** | Jupyter Notebook / Google Colab |
| **Model Serialization** | joblib (.pkl) |
| **Validation Dataset** | UNSW-NB15 (University of New South Wales) |

---

## 📂 Project Structure

```
AI-SOC-Alert-Framework/
│
├── data/
│   ├── soc_alerts.csv                  # Synthetic SOC alert dataset (1,000 records)
│   ├── UNSW_NB15_training-set.csv      # Real-world training data (82,332 records)
│   └── UNSW_NB15_testing-set.csv       # Real-world testing data (175,341 records)
│
├── model/
│   ├── soc_alert_model.pkl             # Trained Random Forest model (synthetic)
│   ├── label_encoder.pkl               # Label encoder for severity classes (synthetic)
│   ├── soc_model_real_data.pkl         # Trained Random Forest model (real data)
│   └── label_encoder_real.pkl          # Label encoder for severity classes (real data)
│
├── notebooks/
│   ├── soc_alert_ml.ipynb              # Original training, evaluation & analysis notebook
│   └── real_data_test.ipynb            # Real-world UNSW-NB15 validation notebook
│
├── screenshots/
│   ├── dataset_preview.png             # Dataset structure overview
│   ├── confusion_matrix.png            # Model performance matrix (synthetic)
│   ├── feature_importance.png          # Feature contribution analysis
│   ├── severity_distribution.png       # Alert class distribution (synthetic)
│   ├── workload_reduction.png          # Analyst workload impact chart (synthetic)
│   ├── real_severity_distribution.png  # Alert class distribution (real data)
│   ├── real_confusion_matrix.png       # Model performance matrix (real data)
│   └── synthetic_vs_real.png           # Accuracy comparison chart
│
├── report/
│   └── AI_SOC_Report_Final.docx        # Full project report
│
├── app.py                              # CLI SOC alert triage system
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── .gitignore
```

---

## 🚀 Key Capabilities

| Capability | Description |
|------------|-------------|
| 🤖 **Automated Classification** | Classifies every incoming alert without analyst input |
| ⚡ **Real-time Prioritization** | Ranks alerts by severity for immediate decision-making |
| 🛡️ **Response Recommendations** | Provides actionable remediation steps per severity level |
| 📊 **Performance Evaluation** | Full metrics including accuracy, confusion matrix, and classification report |
| 🔍 **Feature Importance Analysis** | Identifies which signals most strongly predict threat severity |
| 📉 **Workload Reduction Modelling** | Quantifies the operational impact on analyst bandwidth |
| 🌍 **Real-World Validated** | Tested against 175,341 records from the UNSW-NB15 benchmark dataset |

---

## 🧪 Use Cases

- ✅ **SOC Tier-1 Alert Triage Automation** — Replace manual Level 1 screening with ML classification
- ✅ **Security Alert Prioritization Systems** — Ensure critical threats are never buried in noise
- ✅ **SIEM Integration Enhancement** — Augment platforms like Splunk or Elastic Security
- ✅ **Threat Detection Pipelines** — Feed predictions into broader detection workflows
- ✅ **AI-Assisted Incident Response** — Speed up analyst decision-making with automated context

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/rohit-aswal08/AI-SOC-Alert-Framework.git
cd AI-SOC-Alert-Framework
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the CLI Alert Triage System
```bash
python app.py
```

### 4. Open the Original Training Notebook
```bash
jupyter notebook notebooks/soc_alert_ml.ipynb
```

### 5. Open the Real-World Validation Notebook
```bash
jupyter notebook notebooks/real_data_test.ipynb
```

---

## 📋 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
joblib
```

> Install all at once: `pip install -r requirements.txt`

---

## 🧑‍💻 Skills Demonstrated

- ✅ Machine Learning Classification (Random Forest)
- ✅ Real-World Dataset Validation (UNSW-NB15 — 175,341 records)
- ✅ Feature Engineering & Cross-Dataset Column Mapping
- ✅ SOC Alert Triage Logic & Prioritization
- ✅ Automated Incident Response System Design
- ✅ Security Data Analysis & Feature Engineering
- ✅ Python Development & Model Serialization
- ✅ Threat Detection & Multi-class Classification
- ✅ Performance Evaluation & Metrics Reporting
- ✅ Data Visualization for Cybersecurity Insights

---

## 🔮 Future Enhancements

- 🔗 Integration with SIEM platforms (Splunk, Elastic Security, IBM QRadar)
- 🧠 Explore Deep Learning models (LSTM for temporal alert sequences)
- 🌲 Benchmark against XGBoost, LightGBM, and ensemble methods
- 🌐 REST API wrapper for SIEM/SOAR platform integration
- 📊 Real-time dashboard for live SOC monitoring
- 🗂️ Expand validation to CICIDS and additional benchmark datasets

---

## ⚠️ Disclaimer

> This project uses **synthetically generated SOC alert data** for initial training and evaluation, and has been subsequently validated against the **UNSW-NB15 real-world network dataset** (University of New South Wales Canberra). It is intended as a proof-of-concept framework and a demonstration of AI-driven triage logic. No real organisational or sensitive data was used.

---

## 👨‍💻 Author

<div align="center">

**Rohit Aswal**

🔐 Cybersecurity & Machine Learning Enthusiast  
📌 Independent Project

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rohit-aswal08)

</div>

---

<div align="center">

⭐ **If you found this project useful, consider giving it a star!** ⭐

*Built independently with a focus on practical SOC automation using machine learning.*  
*Validated against 175,341 real-world network records from the UNSW-NB15 benchmark dataset.*

</div>
