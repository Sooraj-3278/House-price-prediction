import streamlit as st
import pickle

# Load trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Website title
st.title("🏠 House Price Prediction System")

st.write("Enter house details to predict the price")

# Input fields
area = st.number_input("Area (in sq ft)", min_value=500, max_value=5000, step=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
location = st.slider("Location Rating (1 = Poor, 5 = Excellent)", 1, 5)

# Prediction button
if st.button("Predict Price"):
    price = model.predict([[area, bedrooms, bathrooms, location]])
    st.success(f"Predicted House Price: ₹ {int(price[0])}")
