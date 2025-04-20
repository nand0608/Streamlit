import streamlit as st
def main():
    number = st.slider("pick a number",0,100,10)
    st.write(f"You picked: {number}")
    st.write(f"square:a {number*number}")
if __name__ == '__main__':
    main()