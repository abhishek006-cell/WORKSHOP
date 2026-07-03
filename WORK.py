import streamlit as st
# take a user input 
st.title("take the input")

name=st.text_input("enter your name")



if st.button("subjects"):
  st.write(f"print the name:{name}")
