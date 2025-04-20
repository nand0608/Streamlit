import streamlit as st
def main():
    wpnumber = st.sidebar.text_input("enter your wp number")
    st.write(f"you selected frome sidebar : {wpnumber}")
if __name__ == '__main__':
    main()