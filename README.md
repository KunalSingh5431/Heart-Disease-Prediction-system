# ❤️ Heart Disease Prediction System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellowgreen)

## 📋 Project Overview

The **Heart Disease Prediction System** is a web application that uses a machine learning model to predict the likelihood of a user having heart disease based on various health parameters. Built with `Streamlit`, this user-friendly interface allows individuals to input their data and receive instant predictions.

## 🚀 Features

- 🌟 **Interactive User Interface**: Built with Streamlit for a clean and interactive UI.
- 🧠 **Machine Learning Model**: Uses a pre-trained machine learning model to provide predictions.
- 📊 **User Data Input**: Multiple input methods including sliders, number inputs, and dropdowns.
- 🔍 **Real-Time Prediction**: Instantly displays prediction results with visual cues (icons and colors).

## 🛠️ Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KunalSingh5431/heart-disease-prediction-system.git
   cd heart-disease-prediction-system
   ```
2. **Install the Required Packages:**
   ```bash
    pip install -r requirements.txt
   ```
3.**Run the Streamlit Application:**
   ``` bash
   streamlit run app.py
   ```

## 📥 Usage
1) Open your web browser and go to http://localhost:8501.
2) Fill in the patient data on the sidebar.

## 🎯 Input Parameters
The app requires the following input parameters for prediction:

1) **Age:** Age of the patient in years.
2) **Sex:** Gender of the patient.
3) **Chest Pain Type:** Type of chest pain experienced (0-3).
4) **Resting Blood Pressure:** Resting blood pressure in mm Hg.
5) **Serum Cholesterol:** Serum cholesterol in mg/dl.
6) **Fasting Blood Sugar:** Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
7) **Resting ECG Results:** Resting electrocardiographic results (0-2).
8) **Max Heart Rate Achieved:** Maximum heart rate achieved.
9) **Exercise Induced Angina:** Presence of exercise-induced angina (1 = yes; 0 = no).
10) **ST Depression Induced by Exercise:** Value of ST depression induced by exercise relative to rest.
11) **Slope of the Peak Exercise ST Segment:** Slope of the peak exercise ST segment (0-2).
12) **Number of Major Vessels Colored by Flourosopy:** Number of major vessels (0-4).
13) **Thalassemia:** A blood disorder (0-3).

## 🧪 Model Details
1) The model used in this project is a pre-trained machine learning model (e.g., Logistic Regression, Random Forest, etc.) trained on a heart disease dataset. The model predicts the presence or absence of heart disease based on the provided input parameters.
2) **Model Accuracy** : 85%

## 📚 How it Works
1) The user provides input via the web interface.
2) The input data is fed into the machine learning model.
3) The model outputs a prediction, which is displayed to the user along with visual feedback (icons and colors).

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1) Fork the Repository
2) Create your Feature Branch (git checkout -b feature/AmazingFeature)
3) Commit your Changes (git commit -m 'Add some AmazingFeature')
4) Push to the Branch (git push origin feature/AmazingFeature)
5) Open a Pull Request

## 🙏 Acknowledgments
1) Thanks to the `UCI Machine Learning Repository` for providing the dataset.
2) Streamlit for an amazing framework for building web apps.
3) All contributors and supporters!

## 📧 Contact
Kunal Singh - kunalsingh5431@gmail.com
