import streamlit as st
import pandas as pd
import joblib
import spreadsheet  # Your spreadsheet.py
import openpyxl

# Load the trained model
model = joblib.load("SafeOrNot_model.pkl")

# App title
st.title("💧 Water Safety Prediction App")
st.write("Automatically predicting water safety from spreadsheet data...")

# Fetch data automatically from spreadsheet.py
reqLoc = spreadsheet.findMatch()  # Make sure findMatch() returns [EC, Cl, SO4, Fe, As]

if not reqLoc or len(reqLoc) < 5:
    st.error("No data found in spreadsheet!")
else:
    # Map the list to your model's features
    sample = pd.DataFrame([{
        "EC (µS/cm at": reqLoc[0],
        "Cl (mg/L)": reqLoc[1],
        "SO4": reqLoc[2],
        "Fe (ppm)": reqLoc[3],
        "As (ppb)": reqLoc[4]
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
