import pickle

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

area = float(input("Enter area (sq ft): "))
bedrooms = int(input("Enter bedrooms: "))
bathrooms = int(input("Enter bathrooms: "))
location = int(input("Enter location rating (1-5): "))

price = model.predict([[area, bedrooms, bathrooms, location]])

print("Predicted House Price: ₹", int(price[0]))
