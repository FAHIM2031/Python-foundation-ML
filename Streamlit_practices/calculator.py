import streamlit as st
def calculator(a,b,operation):
    if operation=="Addition":
        return a+b
    elif operation=="Substraction":
        return a-b
    elif operation=="Multiplication":
        return a*b
    elif operation=="Division":
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"


st.title("Simple calculator")

a=st.number_input("Enter First number",value=0,placeholder="First number")
b=st.number_input("Enter Second number",value=0,placeholder="Second number")
operation=st.selectbox("select operation",["Addition","substraction","Multiplication","Division"])
click=st.button("Calculate")

if click:
    result= calculator(a,b,operation)
    st.write("Result = ",result)