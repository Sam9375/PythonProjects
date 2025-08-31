import streamlit as st
name = st.text_input('please enter your name: ')
red_marbles = st.number_input('please enter the amount of red marbles you have: ',0)
blue_marbles = st.number_input('please enter the amount of blue marbles you have: ',0)
green_marbles = st.number_input('please enter the amount of green marbles you have: ',0)
total = green_marbles + blue_marbles + red_marbles
if st.button('Check Amount Of Marbles'):
    st.write (name,'you have',total,'marbles')

