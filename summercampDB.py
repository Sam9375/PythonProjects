import streamlit as st

name = st.text_input('please enter your name: ')
col1, col2, = st.columns(2)

with col1:
    python = st.number_input('please enter your python score: ')
    web_dev = st.number_input('please enter your web development score: ')

with col2:
    robotics = st.number_input('please enter your robotics score: ')
    prob_solving = st.number_input('plese enter yor robotics score: ')

total = python + web_dev + robotics + prob_solving
average = total/4

if average >= 90:
            grade = 'A+'
            badge = 'platinum'
elif average >= 80:
            grade = 'A'
            badge = 'Gold'
elif average >= 70:
            grade = 'B'
            badge = 'Silver'
elif average >= 60:
            grade = 'C'
            badge = 'Bronze'
elif average >= 50:
            grade = 'D'
            badge = 'participant'
elif average >= 40:
            grade = 'F'
            badge = 'participant'

if st.button('check score'):
        if badge == 'platinum':
                 st.write(name,'your grade is',grade,'and your badge is',badge,'congratulations!')
                 st.balloons()
        else:
                 st.write(name,'your grade is',grade,'and your badge is',badge)


       

  





 
