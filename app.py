import streamlit as st
import pickle as pk
import pandas as pd
import time as t
model=pk.load(open('model_pickle_heart.pkl','rb'))
st.title('HEART DISEASES PREDICTION')
age = st.number_input(':red[Enter Your Age : ]')
gen = st.radio(':red[Enter Your Gender Male Or Female : ]',('Gender','Male','Female'))
gender=0.0
if gen == 'Male':
    gender = 1.0
elif(gen == 'Female'):
    gender = 0.0
else:
    st.write(':green[Please Enter Your Gender]')
cp = st.number_input(':red[Enter Your cp : ]')   
trestbps = st.number_input(':red[Enter Your Trestbps : ]')
chol = st.number_input(':red[Enter Your chol : ]')
fbs = st.number_input(':red[Enter Your fbs : ]')
restecg = st.number_input(':red[Enter Your restecg : ]')
thalach = st.number_input(':red[Enter Your thalach : ]')
exang = st.number_input(':red[Enter Your exang : ]')
oldpeak = st.number_input(':red[Enter Your Oldpeak : ]')
slope = st.number_input(':red[Enter Your slope : ]')
ca = st.number_input(':red[Enter Your ca : ]')
thal= st.number_input(':red[Enter Your thal : ]')

age= int(age)
sex= int(gender)
cp= int(cp)
trestbps= int(trestbps)
chol = int(chol)
fbs= int(fbs)
restecg= int(restecg)
thalach= int(thalach)
exang= int(exang)
oldpeak= int(oldpeak)
slope=int(slope)
ca= int(ca)
thal= int(thal)

if st.button('Predict'):
    with st.spinner('Wait for evaluation...'):
        t.sleep(5)
        
    
    res = model.predict(pd.DataFrame({'age': age,'sex': gender,'cp' : cp,'trestbps' : trestbps,'chol' : chol,
                     'fbs': fbs,'restecg' : restecg ,'thalach' : thalach,'exang' : exang,'oldpeak' : oldpeak,
                     'slope' : slope,'ca' : ca,'thal' : thal},index=[0]))
    if res == 0:
        st.balloons()
        st.header(':green[No Heart-Disease]')
    else:
        st.snow()
        t.sleep(1)
        st.header(':green[Heart Disease Is Detected]')



