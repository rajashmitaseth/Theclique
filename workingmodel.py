import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("SafeOrNot_model.pkl")

# Set the title
st.title("💧 Water Safety Prediction App")
st.write("Enter water parameters below to check if it's safe for drinking.")

# Input fields for the 9 parameters
pH = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
EC = st.number_input("EC (µS/cm at)", min_value=0.0, step=1.0)
Hardness = st.number_input("Hardness (mg/L)", min_value=0.0, step=1.0)
NO3 = st.number_input("Nitrate (NO3) (mg/L)", min_value=0.0, step=0.1)
Cl = st.number_input("Chloride (Cl) (mg/L)", min_value=0.0, step=0.1)
F = st.number_input("Fluoride (F) (mg/L)", min_value=0.0, step=0.01)
SO4 = st.number_input("Sulphate (SO4) (mg/L)", min_value=0.0, step=0.1)
Fe = st.number_input("Iron (Fe) (ppm)", min_value=0.0, step=0.01)
As = st.number_input("Arsenic (As) (ppb)", min_value=0.0, step=0.01)

# Prediction button
if st.button("Check Water Safety"):
    # Create a dataframe for the input
    sample = pd.DataFrame([{
        "pH": pH,
        "EC (µS/cm at": EC,
        "Hardness": Hardness,
        "NO3": NO3,
        "Cl (mg/L)": Cl,
        "F (mg/L)": F,
        "SO4": SO4,
        "Fe (ppm)": Fe,
        "As (ppb)": As
    }])

    # Make prediction
    prediction = model.predict(sample)[0]

    # Suggest alternatives
    def suggest_alternatives(label):
        if label == "Drinking":
            return ["Drinking", "Cooking", "Household use"]
        elif label == "Irrigation":
            return ["Irrigation", "Livestock use"]
        elif label == "Industrial":
            return ["Cooling water", "Construction", "Non-sensitive cleaning"]
        else:
            return ["Construction (cement mixing, road work)", "Non-sensitive industrial uses"]

    st.subheader(f"Prediction: {prediction}")
    st.write("### Suggested uses:")
    for use in suggest_alternatives(prediction):
        st.write(f"- {use}")
