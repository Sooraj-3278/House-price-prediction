import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("house_data.csv")

X = data[['Area', 'Bedrooms', 'Bathrooms', 'Location']]
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")
