import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Title of the Streamlit app
st.write("""
# Insurance Premium Prediction App

This app predicts the *insurance premium* based on the user's age, height, and weight.
""")

# Sidebar for user input parameters
st.sidebar.header('User Input Parameters')

# Function to get user input from the sidebar (using sliders for age, height, and weight)
def user_input_features():
    age = st.sidebar.slider('Age', 18, 100, 30)  # Slider for age input
    height = st.sidebar.slider('Height (cm)', 140, 200, 165)  # Slider for height input
    weight = st.sidebar.slider('Weight (kg)', 40, 120, 70)  # Slider for weight input
    return age, height, weight

# Get user input
age, height, weight = user_input_features()

# Display the user input in the app
st.subheader('User Input parameters')
st.write(f"Age: {age} years, Height: {height} cm, Weight: {weight} kg")

# Load the dataset
df = pd.read_csv("insurance2.csv")  # Update this path with the correct file path

# Fill missing values in 'height' column with the mean
m = df.height.mean()
df.height = df.height.fillna(m)

# Prepare the data for training
X = df[['Age', 'height', 'weight']]  # Features: Age, height, and weight
y = df['premium']  # Target: Premium

# Train the Linear Regression model
lr = linear_model.LinearRegression()
lr.fit(X, y)

# Prediction for the user's input (age, height, weight)
prediction = lr.predict([[age, height, weight]])

# Display the predicted premium for the user's input
st.subheader('Predicted Premium')
st.write(f"Insurance Premium for age {age}, height {height} cm, weight {weight} kg: ${prediction[0]:.2f}")

# Display the model accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=51)
accuracy = lr.score(X_test, y_test)
st.subheader('Model Accuracy')
st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

# Additional Predictions for other specific inputs (for comparison)
ans1 = lr.predict([[27, 167.56, 60]])  # Age 27, height 167.56 cm, weight 60 kg
ans2 = lr.predict([[60, 165.10, 80]])  # Age 60, height 165.10 cm, weight 80 kg

# Display additional predictions
st.subheader('Additional Predictions')
st.write(f"Predicted Premium for age 27, height 167.56 cm, weight 60 kg: ${ans1[0]:.2f}")
st.write(f"Predicted Premium for age 60, height 165.10 cm, weight 80 kg: ${ans2[0]:.2f}")

# Prediction for the first test record (just for comparison)
ansfor1strec = lr.predict(X_test[0:1])
st.write(f"Predicted Premium for the first test record: ${ansfor1strec[0]:.2f}")

# Optionally, you can predict premiums for all test records (though it’s not displayed)
st.write("Predict Premiums for All Test Records:")
st.write(lr.predict(X_test))

