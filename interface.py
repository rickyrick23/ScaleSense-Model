import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('nutrition_advice_model.joblib')
scaler = joblib.load('scaler.joblib')

# Streamlit interface for user input
st.title('Nutrition Advice and Exercise Recommendation')

# Create user input fields with consistent types (float)
age = st.number_input('Age', min_value=10, max_value=100, value=25.0, step=1.0)
gender = st.selectbox('Gender', ['Male', 'Female'])
height = st.number_input('Height (cm)', min_value=50.0, max_value=250.0, value=170.0, step=0.1)
weight = st.number_input('Weight (kg)', min_value=20.0, max_value=200.0, value=70.0, step=0.1)
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=24.2, step=0.1)
body_fat = st.number_input('Body Fat (%)', min_value=1.0, max_value=50.0, value=18.0, step=0.1)
muscle = st.number_input('Muscle (%)', min_value=1.0, max_value=50.0, value=40.0, step=0.1)
protein = st.number_input('Protein (%)', min_value=1.0, max_value=50.0, value=30.0, step=0.1)
visceral_fat = st.number_input('Visceral Fat', min_value=1.0, max_value=20.0, value=10.0, step=0.1)
water_percentage = st.number_input('Water (%)', min_value=30.0, max_value=100.0, value=60.0, step=0.1)
bmr = st.number_input('BMR (kcal)', min_value=100.0, max_value=5000.0, value=1500.0, step=1.0)
daily_calorie_target = st.number_input('Daily Calorie Target', min_value=1000.0, max_value=5000.0, value=2500.0, step=1.0)
carbs = st.number_input('Carbs (%)', min_value=0.0, max_value=100.0, value=50.0, step=0.1)
protein_intake = st.number_input('Protein Intake (%)', min_value=0.0, max_value=100.0, value=20.0, step=0.1)
fat = st.number_input('Fat (%)', min_value=0.0, max_value=100.0, value=30.0, step=0.1)

# Prepare the input data
input_data = {
    'Age': age,
    'Gender': gender,
    'Height (cm)': height,
    'Weight (kg)': weight,
    'BMI': bmi,
    'Body Fat (%)': body_fat,
    'Muscle (%)': muscle,
    'Protein (%)': protein,
    'Visceral Fat': visceral_fat,
    'Water (%)': water_percentage,
    'BMR (kcal)': bmr,
    'Daily Calorie Target': daily_calorie_target,
    'Carbs (%)': carbs,
    'Protein Intake (%)': protein_intake,
    'Fat (%)': fat
}

# Map the 'Gender' feature
input_data['Gender'] = 0 if input_data['Gender'] == 'Male' else 1

# Convert the input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Scale the input data
input_scaled = scaler.transform(input_df)

# Prediction function to use the trained model
def predict(input_scaled):
    # Predict the exercise recommendation
    recommendation = model.predict(input_scaled)
    return recommendation[0]  # Return the predicted exercise recommendation

# Display the prediction result
if st.button('Get Recommendation'):
    recommendation = predict(input_scaled)
    st.write(f"Recommended Exercise: {recommendation}")
