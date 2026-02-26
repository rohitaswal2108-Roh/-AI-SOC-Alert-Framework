# AI-Driven SOC Alert Prioritization & Response Framework

A machine learning system that automatically classifies security alerts,
prioritizes threats, and suggests remediation actions for SOC analysts.

---

## Problem Statement

SOC analysts face alert fatigue due to high volumes of security events.
Manual triage is slow, error-prone, and unsustainable at scale.
This system automates alert prioritization and response recommendations,
reducing analyst workload significantly.

---

## Solution Overview

A Random Forest classification model trained on simulated SOC alert data
that automatically:
- Classifies alerts into Critical / High / Medium / Low severity
- Suggests appropriate remediation actions per severity level
- Measures analyst workload reduction

---

## Results

| Metric | Value |
|---|---|
| Model Accuracy | 97.5% |
| Analyst Workload Reduction | 42.5% |
| Total Alerts Processed | 1000 |
| Auto-handled Alerts | 425 |
| Alerts Requiring Analyst | 575 |

---

## Features Used

| Feature | Description |
|---|---|
| failed_logins | Number of failed login attempts |
| external_ip | Traffic from external IP (0/1) |
| data_transfer_mb | Volume of data transferred |
| malware_flag | Malware signature detected (0/1) |
| dns_beaconing | DNS beaconing detected (0/1) |

---

## Remediation Engine

Each predicted severity triggers automated response suggestions:

- **Critical** - Isolate host, block IP, reset credentials, escalate immediately
- **High** - Investigate IP, reset credentials, review auth logs
- **Medium** - Monitor closely, review user activity
- **Low** - Log and review during next audit

---

## Screenshots

### Dataset Preview
![Dataset](screenshots/dataset_preview.png)

### Severity Distribution
![Distribution](screenshots/severity_distribution.png)

### Confusion Matrix
![Confusion Matrix](screenshots/confusion_matrix.png)

### Feature Importance
![Features](screenshots/feature_importance.png)

### Workload Reduction
![Workload](screenshots/workload_reduction.png)

---

## Tech Stack

- Python
- scikit-learn (Random Forest)
- pandas and numpy
- matplotlib and seaborn
- Jupyter Notebook

---

## Project Structure
```
AI-SOC-Alert-Framework/
│
├── data/
├── notebooks/
│   └── soc_alert_ml.ipynb
├── model/
│   ├── soc_alert_model.pkl
│   └── label_encoder.pkl
├── screenshots/
└── report/
```

---

## Skills Demonstrated

- Machine Learning Classification
- SOC Alert Triage and Prioritization
- Automated Incident Response Logic
- Security Data Analysis
- Python Development
- Threat Detection and Classification

---

## Author

**Rohit Aswal**
