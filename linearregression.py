import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Title of the Streamlit app
st.write("""
# Insurance Premium Prediction App

This app predicts the *insurance premium* based on the user's age.
""")

# Sidebar for user input parameters
st.sidebar.header('User Input Parameters')

# Function to get user input from the sidebar (using slider for age)
def user_input_features():
    age = st.sidebar.slider('Age', 18, 100, 30)  # Slider for age input
    return age

# Get user input
age = user_input_features()

# Display the user input in the app
st.subheader('User Input parameters')
st.write(f"Age: {age} years")

# Load the dataset
df = pd.read_csv("insurance.csv")  # Update this path with the correct file path

# Prepare the data
X = df.iloc[:, 0:1]  # Age column (as the feature)
y = df['premium']    # Premium column (as the target)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=51)

# Train the Linear Regression model
lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)

# Prediction for the user's input age
prediction = lr.predict([[age]])

# Display the predicted premium for the user's age
st.subheader('Predicted Premium')
st.write(f"Insurance Premium for {age} years old: ${prediction[0]:.2f}")

# Display the model accuracy
accuracy = lr.score(X_test, y_test)
st.subheader('Model Accuracy')
st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

# Additional Predictions for other specific ages (for comparison)
ansfor21 = lr.predict([[21]])  # Age 21
ansfor50 = lr.predict([[50]])  # Age 50
ansfor1strec = lr.predict(X_test[0:1])  # First record of test set

# Display additional predictions
st.subheader('Additional Predictions')
st.write(f"Predicted Premium for 21 years old: ${ansfor21[0]:.2f}")
st.write(f"Predicted Premium for 50 years old: ${ansfor50[0]:.2f}")
st.write(f"Predicted Premium for the first test record: ${ansfor1strec[0]:.2f}")
