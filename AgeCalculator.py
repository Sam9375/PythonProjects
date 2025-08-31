import streamlit as st
st.title('Age Calculator')
name = st.text_input('Please Enter Your Name:')
YOB = st.number_input('Please Enter Your Year Of Birth: ',0)
CY = st.number_input('Please Enter Your Current Year: ',0)
age = CY - YOB
st.write(name,'you will be',age,'in',CY)