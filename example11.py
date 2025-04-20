import streamlit as st

if st.checkbox("show/hide"):
    st.text("show")
else:
    st.text("hide")

status = st.radio("what is your status",("Active","inactive"))

if status == "Active":
    st.success("you are active")
else:
    st.warning("inactive")

occupation = st.selectbox("your occupation",["Programmer","Data scientist","Doctor","Business"])
st.write("you selected this option",occupation)

locations = st.multiselect("where is your location",['aus','usa','canada','india','dubai'])
st.write("you selected this option",locations,len(locations),"locations")

first_name = st.text_input("enter ur first name","type here")
if st.button("submit",key = "1"):
    result = first_name.upper()
    st.success(result)

message = st.text_area("enter you message","type here")
if st.button("submit",key = "2"):
    result = message.title()
    st.success(message)

import datetime
today = st.date_input("today is",datetime.datetime.now())
the_time = st.time_input("the time is",datetime.time())


st.balloons()