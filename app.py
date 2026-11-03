"""
IoT with AI Internship — Week 4 Capstone
Streamlit AI-Powered Smart Home Interactive Dashboard
"""

import os
import joblib
import pandas as pd
import numpy as np
import streamlit as st
from mqtt_security import encrypt_payload, decrypt_payload

st.set_page_config(page_title="AI Smart Home Platform", page_icon="🏠", layout="wide")

st.title("🏠 AI-Powered Smart Home Automation Platform")
st.write("Multi-sensor IoT integration, TinyML occupancy prediction, energy optimization, & voice control.")

# Load Trained Models
@st.cache_resource
def load_models():
    if not os.path.exists("occupancy_model.joblib") or not os.path.exists("energy_optimizer_model.joblib"):
        return None, None
    return joblib.load("occupancy_model.joblib"), joblib.load("energy_optimizer_model.joblib")

occupancy_model, energy_model = load_models()

if occupancy_model is None:
    st.error("⚠️ AI Models missing! Please run `python train_ai_models.py` first.")
else:
    # Sidebar Controls & Voice Simulation
    st.sidebar.header("🎙️ Smart Voice Control")
    voice_cmd = st.sidebar.text_input("Enter Voice Command:", "Turn off living room lights and set AC to 22 degrees")
    
    if st.sidebar.button("Execute Voice Command"):
        st.sidebar.success(f" Parsed & Dispatched: '{voice_cmd}'")

    st.sidebar.markdown("---")
    st.sidebar.markdown("🔒 **MQTT Security:** AES-256 Encrypted")
    st.sidebar.markdown("📱 **Mobile Alerts:** ACTIVE (Pushover API)")

    # Main Dashboard Columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🎛️ Multi-Sensor Live Telemetry")
        temp = st.slider("Temperature (°C)", 15.0, 40.0, 25.5, 0.5)
        motion = st.radio("PIR Motion Sensor", [0, 1], format_func=lambda x: "Motion Detected 🚶" if x == 1 else "No Motion 💤")
        light = st.slider("LDR Light Intensity (Lux)", 10.0, 1000.0, 450.0, 10.0)
        sound = st.slider("Mic Sound Level (dB)", 20.0, 100.0, 52.0, 1.0)

        # AES-256 Payload Simulation
        raw_telemetry = {"temperature": temp, "motion": motion, "light": light, "sound": sound}
        encrypted_token = encrypt_payload(raw_telemetry)
        
        with st.expander("🔐 View AES-256 Encrypted MQTT Payload"):
            st.code(encrypted_token, language="text")

    with col2:
        st.subheader("🤖 AI Analytics & Optimization Engine")
        
        input_df = pd.DataFrame([[temp, motion, light, sound]], columns=["temperature", "motion", "light", "sound"])
        occ_pred = occupancy_model.predict(input_df)[0]
        energy_pred = energy_model.predict(input_df)[0]

        st.metric("Predicted Room Occupancy", "OCCUPIED 🟢" if occ_pred == 1 else "VACANT 🔴")
        st.metric("Estimated Energy Load", f"{energy_pred:.2f} kWh")

        st.markdown("---")
        st.subheader("⚡ Automated Energy Saving Actions")
        if occ_pred == 0:
            st.warning("💡 **Room Vacant:** Auto-dimming lights to 10% & switching HVAC to Eco Mode.")
        else:
            st.info("🌡️ **Room Occupied:** Maintaining comfort temperature at 24°C.")