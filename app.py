import streamlit as st
import joblib
import pandas as pd

# Load the saved XGBoost model
model = joblib.load('crop_model.pkl')

st.title("Crop Yield Prediction System")
st.write("Enter the agricultural parameters below to predict the crop yield (Tons/Hectare).")

# Input sliders for the user
temp = st.slider("Temperature (°C)", 15.0, 45.0, 25.0)
humidity = st.slider("Humidity (%)", 30.0, 90.0, 60.0)
rainfall = st.slider("Rainfall (mm)", 50.0, 300.0, 150.0)
soil_moisture = st.slider("Soil Moisture (%)", 20.0, 80.0, 50.0)
nitrogen = st.slider("Nitrogen (N)", 10.0, 150.0, 50.0)
phosphorus = st.slider("Phosphorus (P)", 5.0, 100.0, 30.0)
potassium = st.slider("Potassium (K)", 10.0, 100.0, 40.0)
gdd = st.slider("Growing Degree Days (GDD)", 1.0, 20.0, 5.0)

# Predict button
if st.button("Predict Crop Yield"):
    # Create DataFrame safely matching model feature names
    input_data = pd.DataFrame([[temp, humidity, rainfall, soil_moisture, nitrogen, phosphorus, potassium, gdd]], 
                              columns=model.feature_names_in_)
    
    prediction = model.predict(input_data)

    st.success(f"Predicted Crop Yield: {prediction[0]:.2f} Tons/Hectare")
