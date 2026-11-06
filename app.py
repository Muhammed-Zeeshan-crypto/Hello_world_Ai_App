import streamlit as st
import numpy as np
from model import train
st.title("Machine Learning Model")
st.subheader("Simple Linear Regression Model")
model = train()
st.sidebar.header("Input Features")
input_value=st.sidebar.slider("Select a value of x",1,10,1)
input_array=np.array([[input_value]])
prediction=model.predict(input_array)
st.write(f"### Input value: {input_value}")
st.write(f"### Predicted value: {prediction[0]}")