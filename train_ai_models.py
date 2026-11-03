"""
IoT with AI Internship — Week 4 Capstone
AI-Powered Smart Home System - Occupancy & Energy Optimization Training Script
"""

import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Ridge

def generate_smart_home_dataset(n_samples=1200):
    """Generates synthetic multi-sensor telemetry data."""
    np.random.seed(42)
    
    temp = np.random.uniform(18.0, 35.0, n_samples)          # °C
    motion = np.random.choice([0, 1], size=n_samples, p=[0.4, 0.6]) # PIR Sensor
    light = np.random.uniform(50.0, 900.0, n_samples)       # LDR Lux
    sound = np.random.uniform(30.0, 85.0, n_samples)        # Decibels (dB)
    
    # Logic rule for occupancy ground truth
    occupancy = ((motion == 1) & (sound > 45.0) | (light > 400.0)).astype(int)
    
    # Energy target score (0 - 100 kWh estimation scale)
    energy_target = (temp * 1.5) + (occupancy * 25.0) + (light * 0.02) + np.random.normal(0, 2, n_samples)
    
    df = pd.DataFrame({
        "temperature": temp,
        "motion": motion,
        "light": light,
        "sound": sound,
        "occupancy": occupancy,
        "energy_kwh": energy_target
    })
    return df

def train_smart_home_models():
    print("[*] Generating multi-sensor smart home dataset...")
    df = generate_smart_home_dataset()
    
    X = df[["temperature", "motion", "light", "sound"]]
    y_occupancy = df["occupancy"]
    y_energy = df["energy_kwh"]
    
    print("[*] Training Occupancy Prediction Model (Random Forest)...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y_occupancy)
    joblib.dump(clf, "occupancy_model.joblib")
    print("[✔] Exported occupancy_model.joblib")
    
    print("[*] Training Energy Optimization Model (Ridge Regression)...")
    reg = Ridge()
    reg.fit(X, y_energy)
    joblib.dump(reg, "energy_optimizer_model.joblib")
    print("[✔] Exported energy_optimizer_model.joblib")

if __name__ == "__main__":
    train_smart_home_models()