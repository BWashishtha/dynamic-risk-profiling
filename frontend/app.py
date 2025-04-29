import streamlit as st
import requests

# Backend API URL
API_URL = "http://localhost:8000/evaluate"  # (change later when deployed)

st.title("🛡️ Dynamic Risk Profiling Dashboard")

st.write("Enter transaction details to evaluate risk score:")

# User Inputs
amount = st.number_input("Transaction Amount ($)", min_value=1.0, max_value=10000.0, value=100.0)
typing_speed = st.slider("Typing Speed (words per minute)", min_value=20, max_value=100, value=50)
touch_pressure = st.slider("Touch Pressure (arbitrary units)", min_value=0.5, max_value=1.5, value=1.0)
timestamp = st.text_input("Timestamp (YYYY-MM-DD HH:MM:SS)", value="2025-04-28 16:20:00")

if st.button("Evaluate Risk"):
    payload = {
        "transaction_amount": amount,
        "typing_speed": typing_speed,
        "touch_pressure": touch_pressure,
        "timestamp": timestamp
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Risk Score: {result['risk_score']}")
            st.info(f"Risk Level: {result['risk_level']}")
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"API Error: {e}")
