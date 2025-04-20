import streamlit as st
def main():
    optionmenu = st.sidebar.selectbox("How would you like to contacted?",('email','homephone','phone'))
    st.write(f"you selected from sidebar:-{optionmenu}")
if __name__ == '__main__':
    main()