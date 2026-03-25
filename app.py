import argparse
import os
import sys
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = os.path.join("model", "soc_alert_model.pkl")
ENCODER_PATH = os.path.join("model", "label_encoder.pkl")

FEATURE_COLUMNS = [
    "failed_logins",
    "external_ip",
    "data_transfer_mb",
    "malware_flag",
    "dns_beaconing",
]

PLAYBOOKS = {
    "Critical": [
        "ISOLATE affected host",
        "BLOCK external IP",
        "RESET credentials",
        "ESCALATE immediately",
    ],
    "High": [
        "Investigate alert source",
        "Review logs",
        "Enable monitoring",
    ],
    "Medium": [
        "Monitor activity",
        "Check related alerts",
    ],
    "Low": [
        "Log alert",
        "No immediate action",
    ],
}


def load_model():
    if not os.path.exists(MODEL_PATH):
        print("Model not found")
        sys.exit(1)
    if not os.path.exists(ENCODER_PATH):
        print("Encoder not found")
        sys.exit(1)

    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder


def predict(model, encoder, alert):
    df = pd.DataFrame([alert], columns=FEATURE_COLUMNS)

    proba = model.predict_proba(df)[0]
    pred = model.classes_[np.argmax(proba)]
    severity = encoder.inverse_transform([pred])[0]

    return severity


def demo(model, encoder):
    alert = {
        "failed_logins": 45,
        "external_ip": 1,
        "data_transfer_mb": 900,
        "malware_flag": 1,
        "dns_beaconing": 1,
    }

    severity = predict(model, encoder, alert)

    print("\n=== DEMO ALERT ===")
    print(alert)
    print(f"\nPredicted Severity: {severity}")

    print("\nActions:")
    for step in PLAYBOOKS[severity]:
        print("-", step)


def interactive(model, encoder):
    alert = {
        "failed_logins": int(input("failed_logins: ")),
        "external_ip": int(input("external_ip (0/1): ")),
        "data_transfer_mb": int(input("data_transfer_mb: ")),
        "malware_flag": int(input("malware_flag (0/1): ")),
        "dns_beaconing": int(input("dns_beaconing (0/1): ")),
    }

    severity = predict(model, encoder, alert)

    print("\nPredicted Severity:", severity)


def batch(model, encoder, path):
    df = pd.read_csv(path)

    preds = []
    for _, row in df.iterrows():
        alert = row[FEATURE_COLUMNS].to_dict()
        preds.append(predict(model, encoder, alert))

    df["predicted_severity"] = preds

    print("\nBatch Prediction Summary:")
    print(df["predicted_severity"].value_counts())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--csv", type=str)

    args = parser.parse_args()

    model, encoder = load_model()

    if args.csv:
        batch(model, encoder, args.csv)
    elif args.interactive:
        interactive(model, encoder)
    else:
        demo(model, encoder)