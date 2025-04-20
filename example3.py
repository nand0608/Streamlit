import streamlit as st
def main():
    if st.button ("say hello"):
        st.write("hi hello there!")
    else: 
        st.write("goodbye")
if __name__ == '__main__':
    main()