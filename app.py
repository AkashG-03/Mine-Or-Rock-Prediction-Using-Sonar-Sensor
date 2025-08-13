import streamlit as st
import numpy as np
import pickle


model = pickle.load(open('sonar_model.pkl', 'rb'))


st.title("Sonar Rock vs Mine Prediction")
st.write("Enter the 60 values from sonar sensor to predict whether it's a Rock or Mine.")


input_data = []
for i in range(60):
    value = st.number_input(f"Feature {i+1}", format="%.4f", step=0.01)
    input_data.append(value)


if st.button("Predict"):
    
    input_data_np = np.asarray(input_data).reshape(1, -1)
    

    prediction = model.predict(input_data_np)


    if prediction[0] == 'R':
        st.success("The object is a **Rock**")
    else:
        st.success("The object is a **Mine**")
