import pandas as pd
import streamlit as st 
df = pd.read_csv("income.csv")
st.write(f"Displaying {'income.csv'} dataset:")
st.write(df)
st.write("Number of Rows", df.shape[0])
st.write("Number of Columns", df.shape[1])
st.write('Column names and data types ', df.dtypes)
st.write("Summary Statistics ", df.describe())