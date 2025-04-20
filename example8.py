import streamlit as st
def main():
    uploaded = st.sidebar.file_uploader("choose a csv file",type="csv")
if __name__ == '__main__':
    main()