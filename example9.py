import streamlit as st
import pandas as pd
import numpy as np
def main():
    number = st.slider("pick a number",0,100,10)
    st.write(f"You picked: {number}")

    data = pd.DataFrame({
        'first_column': list(range(1,11)),
        'second_column': np.arange(number,number+10)
    })
    st.line_chart(data)
if __name__ == '__main__':
    main()