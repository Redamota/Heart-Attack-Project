import streamlit as st
import pandas as pd
import joblib
from PIL import Image

st.set_page_config(page_title="CardioPulse AI",
                    page_icon="Gemini_Generated_Image_pmjreppmjreppmjr.png",
                      layout="centered")



# Header of Model
model = joblib.load('heart_attack_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title('CardioPulse AI - Heart Attack Prediction')
st.write('This model is a helpful tool for predicting heart attacks with up to 78% accuracy, but it is only a supplement and does not replace consulting a doctor. Therefore, please always consult your doctor.')

# Building the form for user input


st.write('Please fill in the following information to predict the risk of heart attack:')
# integer input
with st.expander('Personal Information', expanded = True) :
   
   age = st.slider('Age', min_value=1, max_value=120, value=50)

   gender_choice = st.selectbox('Gender', options=['Male', 'Female'])
   gender_Male = 1 if gender_choice == 'Male' else 0
   
   bmi = st.number_input('Body Mass Index (BMI)', min_value=10.0, max_value=50.0, value=25.0)

with st.expander('Medical Information', expanded = True) :
   
   col1 , col2 = st.columns(2)
   with col1:
    st.write('Section 1:') 
    resting_blood_pressure = st.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=250, value=120)
    cholesterol = st.number_input('Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
    fasting_blood_sugar = st.slider('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', min_value=0, max_value=1, value=0)
    max_heart_rate = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
    exercise_induced_angina = st.slider('Exercise Induced Angina (1 = Yes, 0 = No)', min_value=0, max_value=1, value=0)

    chest_pain_type = st.selectbox('Chest Pain Type', options=['Asymptomatic' , 'Non-anginal Pain' ,'Atypical Angina' , 'Typical Angina'])
    chest_pain_type_Typical_Angina = 1 if chest_pain_type == 'Typical Angina' else 0
    chest_pain_type_Atypical_Angina = 1 if chest_pain_type == 'Atypical Angina' else 0
    chest_pain_type_Non_Anginal_Pain = 1 if chest_pain_type == 'Non-Anginal Pain' else 0
    
    resting_ecg = st.selectbox('Resting ECG', options=['Normal', 'ST-T Abnormality	', 'Left Ventricular Hypertrophy'])
    resting_ecg_Normal = 1 if resting_ecg == 'Normal' else 0
    resting_ecg_ST_T_Wave_Abnormality = 1 if resting_ecg == 'ST-T Abnormality' else 0
   with col2:
    st.write('Section 2:')
    oldpeak = st.number_input('Oldpeak (ST depression induced by exercise relative to rest)', min_value=0.0, max_value=10.0, value=1.0)
    num_major_vessels = st.slider('Number of Major Vessels (0-3) colored by fluoroscopy', min_value=0, max_value=3, value=0)
    diabetes = st.slider('Diabetes (1 = Yes, 0 = No)', min_value=0, max_value=1, value=0)
    Total_Risk_Factor = st.number_input('Total Risk Factor', min_value=0.0, max_value=3.0, value=0.0)
   
    st_slope = st.selectbox('St_Slope', options=['Flat', 'Up', 'Down'])
    st_slope_Flat = 1 if st_slope == 'Flat' else 0
    st_slope_Up = 1 if st_slope == 'Up' else 0

    thalassemia = st.selectbox('Thalassemia', options=['Fixed Defect', 'Reversible Defect', 'Normal'])
    thalassemia_Fixed_Defect = 1 if thalassemia == 'Fixed Defect' else 0
    thalassemia_Reversible_Defect = 1 if thalassemia == 'Reversible Defect' else 0

with st.expander('Lifestyle Information', expanded = True) :

   stress_level = st.number_input('Stress Level :', min_value=1, max_value=10, value=5)

   family_history = st.slider('Family History of Heart Disease (1 = Yes, 0 = No)', min_value=0, max_value=1, value=0)

   smoking_status = st.selectbox('Smoking Status', options=['Never ', 'Former ', 'Current '])
   smoking_status_Never = 1 if smoking_status == 'Never ' else 0
   smoking_status_Former = 1 if smoking_status == 'Former ' else 0

   alcohol_consumption = st.selectbox('Alcohol Consumption', options=['Heavy', 'Moderate', 'Non-drinker'])
   alcohol_consumption_Heavy = 1 if alcohol_consumption == 'Heavy' else 0
   alcohol_consumption_Moderate = 1 if alcohol_consumption == 'Moderate' else 0

   physical_activity = st.selectbox('Physical Activity', options=['Moderate', 'High', 'Low'])
   physical_activity_Moderate = 1 if physical_activity == 'Moderate' else 0
   physical_activity_High = 1 if physical_activity == 'High' else 0

# Heart of Project : 

if st.button("Predict Heart Attack Risk"):
    input_data = {
        'age': [age],
        'resting_blood_pressure': [resting_blood_pressure],
        'cholesterol': [cholesterol],
        'fasting_blood_sugar': [fasting_blood_sugar],
        'max_heart_rate': [max_heart_rate],
        'exercise_induced_angina': [exercise_induced_angina],
        'oldpeak': [oldpeak],
        'num_major_vessels': [num_major_vessels],
        'bmi': [bmi],
        'family_history': [family_history],
        'diabetes': [diabetes],
        'stress_level': [stress_level],
        'Total_Risk_Factor': [Total_Risk_Factor],
        'gender_Male': [gender_Male],
        'chest_pain_type_Typical_Angina': [chest_pain_type_Typical_Angina],
        'chest_pain_type_Atypical_Angina': [chest_pain_type_Atypical_Angina],
        'chest_pain_type_Non_Anginal_Pain': [chest_pain_type_Non_Anginal_Pain],
        'resting_ecg_Normal': [resting_ecg_Normal],
        'resting_ecg_ST_T_Wave_Abnormality': [resting_ecg_ST_T_Wave_Abnormality],
        'st_slope_Flat': [st_slope_Flat],
        'st_slope_Up': [st_slope_Up],
        'thalassemia_Fixed_Defect': [thalassemia_Fixed_Defect],
        'thalassemia_Reversible_Defect': [thalassemia_Reversible_Defect],
        'smoking_status_Never': [smoking_status_Never],
        'smoking_status_Former': [smoking_status_Former],
        'alcohol_consumption_Heavy': [alcohol_consumption_Heavy],
        'alcohol_consumption_Moderate': [alcohol_consumption_Moderate],
        'physical_activity_Moderate': [physical_activity_Moderate],
        'physical_activity_High': [physical_activity_High]
    }
    
    df_user_input = pd.DataFrame(input_data)
    df_reindex = df_user_input.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df_reindex)
    probabilities = model.predict_proba(df_reindex)

    risk = probabilities[0][1]*100  # Probability of having a heart attack

    if prediction[0] == 1:
        st.error(f"High Risk Detected: The model indicates a potential heart attack risk with a probability of {risk:.1f}%. Please consult a healthcare professional.")
    else:
        st.success(f"Low Risk: The model indicates no immediate heart attack risk. Your risk probability is {risk:.1f}%. Keep up the healthy lifestyle!")
