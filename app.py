import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺")      
st.title("🩺 Diabetes Prediction App")
st.markdown("Enter patient details in the sidebar to predict diabetes risk.")

st.sidebar.header("Patient Information")

age            = st.sidebar.slider("Age", 21, 81)
dpf            = st.sidebar.slider("Diabetes Pedigree Function", 0.078, 2.42)
bmi            = st.sidebar.slider("BMI", 0.0, 67.1)
glucose        = st.sidebar.slider("Glucose Level", 0, 200)
blood_pressure = st.sidebar.slider("Blood Pressure (mm Hg)", 0, 122)
skin_thickness = st.sidebar.slider("Skin Thickness (mm)", 0, 99)
insulin        = st.sidebar.slider("Insulin (mu U/ml)", 0, 846)
pregnancies    = st.sidebar.slider("Pregnancies", 0, 17,)

input_data = np.array([[pregnancies, glucose, blood_pressure,
                         skin_thickness, insulin, bmi, dpf, age]])
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Diabetes  |  Confidence: {probability:.1%}")
    else: 
        st.success(f"✅ Low Risk of Diabetes  |  Confidence: {1 - probability:.1%}")

    st.subheader("Input Summary")
    summary = pd.DataFrame({
        'Feature': ['Pregnancies', 'Glucose', 'Blood Pressure',
                    'Skin Thickness', 'Insulin', 'BMI', 'DPF', 'Age'],
        'Value': [pregnancies, glucose, blood_pressure,
                  skin_thickness, insulin, bmi, round(dpf, 3), age]
    })
    st.dataframe(summary, use_container_width=True)