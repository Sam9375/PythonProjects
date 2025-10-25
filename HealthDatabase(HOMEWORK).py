import streamlit as st

st.title('🩺 Student Health Checkup Tracker')

st.subheader('📖 Scenario:')
st.write('You are assisting the school nurse during the annual student health checkup week. Each student is evaluated in five areas: Body Mass Index (BMI), Vision Test, Fitness Test, Blood Pressure and dental hygiene. Youll use this app to input the scores for each test, and the system will calculate their total health score, average, and health grade. ')
st.write('Your job is to ensure that each student’s record is entered correctly and saved for review.')

name = st.text_input('Please enter your name: ')

BMI = st.number_input('Please enter your score for BMI',0)

VTEST = st.number_input('Please enter your score for vision test',0)

FTEST = st.number_input('Please enter your score for fitness test',0)

BPA = st.number_input('Please enter your score for blood pressure assesment',0)

DH = st.number_input('Please enter your score for dental hygiene',0)


if st.button('Submit Student Scores'):
    total = BMI + VTEST + FTEST + BPA + DH
    average = total / 5

    if average >= 90:
        grade = 'A+'
        score = 'Excellent Health'
        st.write(name,',your grade is',grade,'and your score is',score,'.Awesome work!')
        st.balloons()
    elif average >= 80:
        grade = 'A'
        score = 'Very Good'
        st.write(name,',your grade is',grade,'and your score is',score,'.Nice job!')
    elif average >= 70:
        grade = 'B'
        score = 'Good'
        st.write(name,',your grade is',grade,'and your score is',score,'.Good job!')
    elif average >= 60:
        grade = 'C'
        score = 'Fair'
        st.write(name,',your grade is',grade,'and your score is',score,'.Good job, just try harder next time!')
    elif average >= 50:
        grade = 'D'
        score = 'Needs attention'
        st.write(name,',your grade is',grade,'and your score is',score,'.Keep improving!')
    elif average < 50:
        grade = 'F'
        score = 'Immediate Medical Attention'
        st.write(name,',your grade is',grade,'and your score is',score,'.You tried your best, thats what matters!')
