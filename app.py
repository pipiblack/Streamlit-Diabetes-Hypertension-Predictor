import streamlit as st

# App title
st.title("Diabetes/Hypertension Diagnostics app")

# Notes Section
st.header("Notes")
# patients Data
st.write("Please enter the patient's data below:")

Patients_Age = st.number_input("Age", 0, 100, 25)
Gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
Diabetes = st.selectbox("Diabetes", options=["Yes", "No"])
Heart_Disease = st.selectbox("Heart Disease", options=["Yes", "No"])
Smoking_History = st.selectbox("Smoking History", options=["No Info", "Current", "Never", "Past"])
BMI = st.number_input("BMI", 0.0, 100.0, 25.0)
HbA1c_Level = st.number_input("HbA1c Level", 0.0, 100.0, 25.0)
Blood_Glucose_Level = st.number_input("Blood Glucose Level", 0.0, 100.0, 25.0)


doctors_notes = st.text_area(
    "Doctors_Notes", "Cough for 5 days, fever for 3 days, difficulty in breathing for 1 day.")

# Vitals Section
st.header("Vitals")

# Temperature Input
temperature = st.number_input("Temperature (°C)", value=37.0, step=0.1)

# Blood Pressure Input
# systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", value=92)
# diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", value=56)

# # Respiration Rate Input
# respiration_rate = st.number_input("Respiration Rate (cpm)", value=30)

# # Pulse Input (assuming it was missing in the image)
# pulse = st.text_input("Pulse", "Not specified")

# # SpO2 Input
# spo2 = st.slider("SpO2 (%) on room air", min_value=0, max_value=100, value=90)

# # Display the collected information
# st.subheader("Collected Information")
# st.write(f"**Prescriber's Notes:** {doctors_notes}")
# st.write(f"**Temperature:** {temperature} °C")
# st.write(f"**Blood Pressure:** {systolic_bp}/{diastolic_bp} mmHg")
# st.write(f"**Respiration Rate:** {respiration_rate} cpm")
# st.write(f"**Pulse:** {pulse}")
# st.write(f"**SpO2:** {spo2} %")
