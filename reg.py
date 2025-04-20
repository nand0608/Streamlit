import streamlit as st

st.title('Registration')

name = st.text_input('Enter your name')
st.write(name)
age = st.number_input('Enter your age')
st.write(age)
email = st.text_input('Enter your email')
st.write(email)
gen = st.radio("what is your gender", ('male','female'))
st.write(f"you selected:- {gen}")

city = st.selectbox("your city",["unjha","mehsana","patan","unava"])
st.write("your city :-",city)

st.balloons()