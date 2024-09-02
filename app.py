import streamlit as st
import pandas as pd
import pickle
import os
import warnings

warnings.filterwarnings("ignore")

# Determine the path to the model file
if os.path.exists('trained_model.sav'):
    # Path when running locally or in the same directory
    model_path = 'trained_model.sav'
else:
    # Path when running on your local machine with a specific path
    model_path = 'C:/Users/LENOVO/Music/ML Projects/heart_disease/trained_model.sav'

# Load the model using the determined path
model = pickle.load(open(model_path, 'rb'))

st.title('Heart Disease Prediction System')

# Collect user input
def get_user_input():
    st.sidebar.header("📝 Patient Data Input")
    
    # Divide layout into columns
    col1, _, col2 = st.columns([1, 0.2, 1])

    with col1:
        age = st.slider('Age', 20, 80, 50, help="Select the patient's age")
        sex = st.selectbox('Sex', ('Male', 'Female'), help="Select the patient's gender")
        cp = st.slider('Chest Pain Type (0-3)', 0, 3, 1, help="Type of chest pain experienced by the patient")
        trestbps = st.number_input('Resting Blood Pressure (in mm Hg)', 80, 200, 120, step=1)
        chol = st.number_input('Serum Cholesterol (in mg/dl)', 120, 400, 200, step=1)

    with col2:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', (0, 1), help="1 if FBS > 120 mg/dl, 0 otherwise")
        restecg = st.slider('Resting ECG (0-2)', 0, 2, 1, help="Resting electrocardiographic results")
        thalach = st.number_input('Max Heart Rate Achieved', 60, 200, 150, step=1)
        exang = st.selectbox('Exercise Induced Angina (1 = Yes, 0 = No)', (0, 1))
        oldpeak = st.number_input('ST Depression Induced by Exercise', 0.0, 5.0, 2.0, step=0.1)

    # Add another row for remaining inputs
    slope = st.slider('Slope of the Peak Exercise ST Segment (0-2)', 0, 2, 1)
    ca = st.slider('Number of Major Vessels Colored by Flourosopy (0-4)', 0, 4, 0)
    thal = st.slider('Thalassemia (0-3)', 0, 3, 2)

    # Create a dataframe for the input
    user_data = {
        'age': age,
        'sex': 1 if sex == 'Male' else 0,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    features = pd.DataFrame(user_data, index=[0])
    return features

# Display user input
user_input = get_user_input()
st.subheader('📊 Patient Data Overview')
st.write(user_input)

# Predict using the model
prediction = model.predict(user_input)

# Display Prediction Results
st.subheader('🧑‍⚕️ Prediction Result')

if prediction[0] == 0:
    st.markdown('<p style="color:red; font-size: 24px; font-weight:bold; "> ❤️ You have a heart disease</p>', unsafe_allow_html=True)
else:
    st.markdown('<p style="color:green; font-size: 24px; font-weight:bold;"> 💚 You do not have a heart disease</p>', unsafe_allow_html=True)
  
