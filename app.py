import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Streamlit UI
st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to check if it's fraudulent or not.")

# User Inputs
amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
time = st.number_input("Transaction Time (in seconds)", min_value=0.0, format="%.2f")

# Dummy inputs for other features (Replace with actual inputs as needed)
features = np.zeros(28)  # Assuming 28 other features

# Add amount & time to feature array
input_data = np.hstack(([time, amount], features))

# Predict
if st.button("Check for Fraud"):    
    prediction = model.predict([input_data])[0]  # 0: Not Fraud, 1: Fraud
    proba = model.predict_proba([input_data])[0][1]  # Fraud Probability
    
    if prediction == 1:
        st.error(f"🚨 Fraudulent Transaction Detected! (Confidence: {proba:.2%})")
    else:
        st.success(f"✅ Legitimate Transaction (Confidence: {100 - proba:.2%})")
