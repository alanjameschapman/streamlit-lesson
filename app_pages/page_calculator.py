import streamlit as st

def calculator_body():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input(
            label="Enter the first integer",
            step=1)
    with col2:
        operation = st.selectbox(
            label="Select operation",
            options=["+", "-", "*", "/"])
    with col3:
        num2 = st.number_input(
            label="Enter the second integer",
            step=2)
    if st.button("Click here to calculate"):
        if num2 == 0 and operation == "/":
            st.error("Division by zero is not allowed")
        else:
            calculator_function(num1, operation, num2)

def calculator_function(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    st.success(f"The result of {num1} {operation} {num2} is **{result}**")