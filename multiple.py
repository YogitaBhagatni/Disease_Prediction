import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

st.markdown(
    """
    <h1 style='text-align:center;'>Health Assistant</h1>
    """,
    unsafe_allow_html=True)

selected=option_menu(
  menu_title=None,
  options=["Home","Predictions","Dataset"],
  icons=["house","book","envelope"],
  menu_icon="cast",
  default_index=0,
  orientation="horizontal",
)

if selected=="Home":
  image = Image.open(r'dataset/dr_img.png')
  st.image(image)
  


if selected=="Predictions":
  # getting the working directory of the main.py
  working_dir = os.path.dirname(os.path.abspath(__file__))

  # loading the saved models

  diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

  heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

  parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

  

  # sidebar for navigation
  with st.sidebar:
      selected = option_menu('Multiple Disease Prediction System',

                             ['Diabetes Prediction',
                              'Heart Disease Prediction',
                              'Parkinsons Prediction'],
                             menu_icon='hospital-fill',
                             icons=['activity', 'heart', 'person'],
                             default_index=0)

  
    
  # Diabetes Prediction Page
  if selected == 'Diabetes Prediction':

      # page title
      st.title('Diabetes Prediction using ML')

      # getting the input data from the user
      col1, col2, col3 = st.columns(3)

      with col1:
          Pregnancies = st.number_input('Number of Pregnancies')
                        

      with col2:
          Glucose = st.number_input('Glucose Level')

      with col3:
          BloodPressure = st.number_input('Blood Pressure value')

      with col1:
          SkinThickness =st.number_input('Skin Thickness value')

      with col2:
          Insulin = st.number_input('Insulin Level')

      with col3:
          BMI = st.number_input('BMI value')

      with col1:
          DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')

      with col2:
          Age = st.number_input('Age of the Person',0,100)


      # code for Prediction
      diab_diagnosis = ''

      # creating a button for Prediction

      if st.button('Diabetes Test Result'):

          user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]

          user_input = [float(x) for x in user_input]

          diab_prediction = diabetes_model.predict([user_input])

          if diab_prediction[0] == 1:
              diab_diagnosis = 'The person is diabetic'
          else:
              diab_diagnosis = 'The person is not diabetic'

      st.success(diab_diagnosis)

  # Heart Disease Prediction Page
  if selected == 'Heart Disease Prediction':
  
      # page title
      st.title('Heart Disease Prediction using ML')
  
      col1, col2, col3 = st.columns(3)
  
      with col1:
          age = st.slider('Age',1,100)
  
      with col2:
          sex = st.slider('Sex 0=female and 1=male',0,1)
  
      with col3:
          cp = st.number_input('Chest Pain types',0,3)
  
      with col1:
          trestbps = st.number_input('Resting Blood Pressure',0,200)
  
      with col2:
          chol = st.number_input('Serum Cholestoral in mg/dl',0,200)
  
      with col3:
          fbs = st.selectbox('Fasting Blood Sugar & gt',["1","0"])
  
      with col1:
          restecg = st.number_input('Resting Electrocardiographic results',0,1)
  
      with col2:
          thalach = st.number_input('Maximum Heart Rate achieved')
  
      with col3:
          exang = st.selectbox('Exercise Induced Angina',["1","0"])
  
      with col1:
          oldpeak = st.number_input('ST depression induced by exercise')
  
      with col2:
          slope = st.number_input('Slope of the peak exercise ST segment',0,2)
  
      with col3:
          ca = st.number_input('Major vessels colored by flourosopy',0,3)
  
      with col1:
          thal = st.slider("thal=> 0 = normal,1 = fixed defect,2 = reversable defect",0,2)
  
      # code for Prediction
      heart_diagnosis = ''
  
      # creating a button for Prediction
  
      if st.button('Heart Disease Test Result'):
  
          user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
  
          user_input = [float(x) for x in user_input]
  
          heart_prediction = heart_disease_model.predict([user_input])
  
          if heart_prediction[0] == 1:
              heart_diagnosis = 'The person is having heart disease'
          else:
              heart_diagnosis = 'The person does not have any heart disease'
  
      st.success(heart_diagnosis)
  
  # Parkinson's Prediction Page
  if selected == "Parkinsons Prediction":
  
      # page title
      st.title("Parkinson's Disease Prediction using ML")
  
      col1, col2, col3, col4, col5 = st.columns(5)
  
      with col1:
          fo = st.number_input('MDVP:Fo(Hz)')
  
      with col2:
          fhi = st.number_input('MDVP:Fhi(Hz)')
  
      with col3:
          flo = st.number_input('MDVP:Flo(Hz)')
  
      with col4:
          Jitter_percent = st.number_input('MDVP:Jitter(%)')
  
      with col5:
          Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
  
      with col1:
          RAP = st.number_input('MDVP:RAP')
  
      with col2:
          PPQ = st.number_input('MDVP:PPQ')
  
      with col3:
          DDP = st.number_input('Jitter:DDP')
  
      with col4:
          Shimmer = st.number_input('MDVP:Shimmer')
  
      with col5:
          Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
  
      with col1:
          APQ3 = st.number_input('Shimmer:APQ3')
  
      with col2:
          APQ5 = st.number_input('Shimmer:APQ5')
  
      with col3:
          APQ = st.number_input('MDVP:APQ')
  
      with col4:
          DDA = st.number_input('Shimmer:DDA')
  
      with col5:
          NHR = st.number_input('NHR')
  
      with col1:
          HNR = st.number_input('HNR')
  
      with col2:
          RPDE = st.number_input('RPDE')
  
      with col3:
          DFA = st.number_input('DFA')
  
      with col4:
          spread1 = st.number_input('spread1')
  
      with col5:
          spread2 = st.number_input('spread2')
  
      with col1:
          D2 = st.number_input('D2')
  
      with col2:
          PPE = st.number_input('PPE')
  
      # code for Prediction
      parkinsons_diagnosis = ''
  
      # creating a button for Prediction    
      if st.button("Parkinson's Test Result"):
  
          user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                        RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                        APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
  
          user_input = [float(x) for x in user_input]
  
          parkinsons_prediction = parkinsons_model.predict([user_input])
  
          if parkinsons_prediction[0] == 1:
              parkinsons_diagnosis = "The person has Parkinson's disease"
          else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
  
      st.success(parkinsons_diagnosis)
if selected=="Dataset":
  selected=option_menu(
  menu_title="Records",
  options=["Diabetes Data","Heart Disease Data","Parkinsons Disease Data"],
  icons=["clipboard-data","clipboard-data","clipboard-data"])

diabetes_data_= pd.read_csv(r'dataset/diabetes.csv')
diabetes_data_ = pd.DataFrame(diabetes_data_)

heart_data_= pd.read_csv(r'dataset/heart.csv')
heart_data_ = pd.DataFrame(heart_data_)

parkinson_data_= pd.read_csv(r'dataset/parkinson.csv')
parkinson_data_ = pd.DataFrame(parkinson_data_)

if selected=="Diabetes Data":
  st.dataframe(diabetes_data_)
if selected=="Heart Disease Data":
  st.dataframe(heart_data_ )
if selected=="Parkinsons Disease Data":
  st.dataframe(parkinson_data_)
  
    
  

 


  

    
