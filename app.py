# 'Processor_Speed', 'RAM_Size', 'Storage_Capacity'
# python3 -m venv venv
# source venv/bin/activate


import streamlit as st
import numpy as np
import joblib

model= joblib.load('rf_model.pkl')

st.title("Laptop Price Prediction")

st.divider()

st.write("Welcome! This tool helps you analyze and compare devices based on three key specifications: **Processor Speed**, which determines how fast your system runs; **RAM Size**, which affects multitasking performance; and **Storage Capacity**, which defines how much data you can store. Use the insights to make smarter tech decisions!")

st.divider()

processor_speed = st.number_input("Processor Speed (in GHz)", value=2.5, step=0.5)
ram_size = st.number_input("RAM Size (in GB)", value=16, step=8)
storage_capacity = st.number_input("Storage Capacity (in GB)", value=512, step=256)

x=[processor_speed, ram_size, storage_capacity]

st.divider()

predition=st.button("Predict Price")

if predition:
  st.balloons()
  x1=np.array(x)

  predition=model.predict([x1])[0]
  st.write(f"The predicted price of the laptop is: ${predition:,.2f}")

else:
  st.write("Please use button to predict the price of the laptop.")

# from google.colab import files
# files.download('rf_model.pkl') .put this when you download