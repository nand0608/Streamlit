import streamlit as st
def main():
        st.title("sqare and cube calulations")
        number = st.number_input("Enter a number")
        operation = st.radio('select operation:',('none','sqare','cube'))
        num = 0
        result = 0
        if operation =='none':
            result = 0
        elif operation =='sqare':
            num = float(number)
            result = num * 2
        else:
            num = float(number)
            result = num * 3
        st.write(f"The result of {operation.lower()} {number} is: {result}")
if __name__ == '__main__':
    main()