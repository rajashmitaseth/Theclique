import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("SafeOrNot_model.pkl")

# App title
st.title("💧 Water Safety Prediction App")
st.write("Enter water parameters below to check if it's safe for drinking.")

# Input fields (only the 5 your model was trained on)
EC = st.number_input("EC (µS/cm at)", min_value=0.0, step=1.0)
Cl = st.number_input("Chloride (Cl) (mg/L)", min_value=0.0, step=0.1)
SO4 = st.number_input("Sulphate (SO4) (mg/L)", min_value=0.0, step=0.1)
Fe = st.number_input("Iron (Fe) (ppm)", min_value=0.0, step=0.01)
As = st.number_input("Arsenic (As) (ppb)", min_value=0.0, step=0.01)

# Prediction button
if st.button("Check Water Safety"):
    # Create a dataframe for the input
    sample = pd.DataFrame([{
        "EC (µS/cm at": EC,
        "Cl (mg/L)": Cl,
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
        elif label == "Unsafe":
            return ["Irrigation", "Construction", "Non-sensitive cleaning"]
        else:
            return ["Further testing required"]

    st.subheader(f"Prediction: {prediction}")
    st.write("### Suggested uses:")
    for use in suggest_alternatives(prediction):
        st.write(f"- {use}")
