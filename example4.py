import streamlit as st
def main():
    gen = st.radio("what is your movie genre?", ('comedy','drama','document'))
    st.write(f"you selected:- {gen}")
if __name__ == '__main__':
    main()