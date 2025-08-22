import streamlit as st
import requests
import numpy as np

import streamlit as st

st.write(st.secrets["api_key"])

'''
# TaxiFareModel front
'''


'''
## Please input ride data
'''

# Collect input from user
date = st.text_input("Enter the date and time (format: 2013-07-06 17:18:00):")
p_long = st.text_input("Enter Pickup Longitude (format: -73.950655):")
p_lat = st.text_input("Enter Pickup Latitude (format: 40.783282):")
d_long = st.text_input("Enter Dropoff Longitude (format: -73.950655):")
d_lat = st.text_input("Enter Dropoff Latitude (format: 40.783282):")
passenger = st.text_input("Enter Passengers (format: 2):")

if st.button("Predict"):
    # Put inputs into same shape as model expects
    url = "https://taxifare.lewagon.ai/predict"
    params = {
        "pickup_datetime": date,
        "pickup_longitude": p_long,
        "pickup_latitude": p_lat,
        "dropoff_longitude": d_long,
        "dropoff_latitude": d_lat,
        "passenger_count": int(passenger),
    }
    response = requests.get(url=url, params=params).json()

    while not params:
        st.stop()

    st.success(f"The predicted result is: {response}")
