# load the model and enter custom data to predict the output

import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

with open('hypertension_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Enter custom data to predict the output
with open('gender_encoder.pkl', 'rb') as f:
    gender_encoder = pickle.load(f)
with open('diabetes_encoder.pkl', 'rb') as f:
    diabetes_encoder = pickle.load(f)
with open('heart_disease_encoder.pkl', 'rb') as f:
    heart_disease_encoder = pickle.load(f)
with open('smoking_history_encoder.pkl', 'rb') as f:
    smoking_history_encoder = pickle.load(f)

# taking user input and transforming
try:
    # inputs from the user
    gender = gender_encoder.transform([input("Enter Sex: ")])[0]
    age = int(input("Enter Age: "))
    diabetes = diabetes_encoder.transform(
        [input("Enter Diabetes result: ")])[0]
    heart_disease = heart_disease_encoder.transform(
        [input("Enter Heart Disease if any: ")])[0]
    smoking_history = smoking_history_encoder.transform(
        [input("Enter Smoking History from the options given: ")])[0]
    bmi = float(input("Enter BMI level: "))
    HbA1c_level = float(input("Enter HbA1c Level: "))
    blood_glucose_level = float(input("Enter Blood Glucose Level: "))

    # Create DataFrame
    data = {
        'gender': [gender],
        'age': [age],
        'diabetes': [diabetes],
        'heart_disease': [heart_disease],
        'smoking_history': [smoking_history],
        'bmi': [bmi],
        'HbA1c_level': [HbA1c_level],
        'blood_glucose_level': [blood_glucose_level]
    }
    custom_df = pd.DataFrame(data)

    # scaling the input values
    features_to_scale = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    scaler = StandardScaler()
    custom_df[features_to_scale] = scaler.fit_transform(
        custom_df[features_to_scale])

    #
    prediction = model.predict(custom_df)
    print("Prediction:", prediction)
    if prediction == 1:
        print("You are at risk of Hypertension and should consult a doctor")
    else:
        print("You are not at risk of Hypertension")

except Exception as e:
    print("An error occurred:", e)
