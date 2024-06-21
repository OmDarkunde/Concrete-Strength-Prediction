import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("Concrete Strength Prediction")

# Input fields
cement = st.number_input("Cement")
blastFurnace = st.number_input("Blast Furnace")
flyAsh = st.number_input("Fly Ash")
water = st.number_input("Water")
superplasticizer = st.number_input("Superplasticizer")
courseAggregate = st.number_input("Course Aggregate")
fineaggregate = st.number_input("Fine Aggregate")
age = st.number_input("Age", min_value=1, step=1)

# Predict button
if st.button("Predict"):
    try:
        # Transform input features
        features = np.array([cement, blastFurnace, flyAsh, water, superplasticizer, courseAggregate, fineaggregate, age]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Display the prediction
        st.success(f"The predicted concrete strength is {prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error in prediction: {e}")

