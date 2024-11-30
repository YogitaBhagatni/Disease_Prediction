import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="‍⚕️")

selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.title("Health Assistance ‍⚕️")

if selected == "Projects":
    # Get working directory and load models
    working_dir = os.path.dirname(os.path.abspath(__file__))
    diabetes_model = pickle.load(open(f"{working_dir}/saved_models/diabetes_model.sav", "rb"))
    heart_disease_model = pickle.load(open(f"{working_dir}/saved_models/heart_disease_model.sav", "rb"))
    parkinsons_model = pickle.load(open(f"{working_dir}/saved_models/parkinsons_model.sav", "rb"))

    selected_project = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0, )
    

    # Function to handle input validation and prediction
    def predict_disease(model, feature_names, user_inputs):
        try:
            # Convert user inputs to floats
            user_inputs = [float(x) for x in user_inputs]

            # Check if all required features are provided
            if len(user_inputs) != len(feature_names):
                raise ValueError(f"Please provide values for all {len(feature_names)} required features.")

            prediction = model.predict([user_inputs])[0]
            diagnosis = "positive" if prediction == 1 else "negative"
            return f"The person is {diagnosis} for {selected_project.lower()}"

        except ValueError as e:
            st.error(str(e))
            return None

    # Diabetes Prediction Page
    if selected_project == "Diabetes Prediction":
        st.title("Diabetes Prediction using ML")

        col1, col2, col3 = st.columns(3)

        # Input fields with placeholders for guidance
        pregnancies = st.text_input("Number of Pregnancies (0-17)", placeholder="Enter a number")
        glucose = st.text_input("Glucose Level (mg/dL)", placeholder="Enter a number")
        blood_pressure = st.text_input("Blood Pressure value (mmHg)", placeholder="Enter a number")
        skin_thickness = st.text_input("Skin Thickness value (mm)", placeholder="Enter a number")
        insulin = st.text_input("Insulin Level (μU/mL)", placeholder="Enter a number (if 0, enter 0)")
        bmi = st.text_input("BMI value (kg/m²)", placeholder="Enter a number")
        diabetes_pedigree_function = st.text_input(
            "Diabetes Pedigree Function value", placeholder="Enter a number (0.0-2.0)"
        )
        age = st.text_input("Age of the Person (years)", placeholder="Enter a number")

        # Button with conditional prediction and error handling
        if st.button("Diabetes Test Result"):
            diagnosis = predict_disease(
                diabetes_model,
                [
                    "Pregnancies",
                    "Glucose",
                    "BloodPressure",
                    "SkinThickness",
                    "Insulin",
                    "BMI",
                    "DiabetesPedigreeFunction",
                    "Age",
                ],
                [
                    pregnancies,
                    glucose,
                    blood_pressure,
                    skin_thickness,
                    insulin,
                    bmi,
                    diabetes_pedigree_function,
                    age,
                ],
            )
            if diagnosis:
                st.success(diagnosis)

    # Heart Disease Prediction Page
    # (Similar structure with prediction function call and error handling)

    # Parkinson
