import streamlit as st
points = 0
st.title('🚑 First Aid Quiz ')
name = st.text_input('Please enter your name: ')

st.info('Question 1 – Nosebleed')
st.write('Your friends nose suddenly starts bleeding 😮')
st.write('what should you do first?')

Q1 = st.selectbox('Choose the correct question',
             ['Çhoose your answer','Tilt their head back and pinch the nose','Tilt their head forward and pinch the nose','Make them lie flat on the ground' ])

if Q1 == 'Tilt their head forward and pinch the nose':
    points += 1
    st.write('Correct',name,',well done!')
elif Q1 == 'Çhoose your answer':
    st.write('Please choose an answer')
else:
    st.write('Incorrect',name,', nice try!')

st.info('Question 2 – Choking')
st.write('Someone is eating and suddenly starts coughing hard, can’t speak, and looks panicked 😨')
st.write('what should you do first?')
Q2 = st.selectbox('Choose the correct question',['Çhoose your answer','Give them water to drink',
                                                 'Perform the Heimlich maneuver','Tell them to lie down and rest'])

if Q2 == 'Perform the Heimlich maneuver':
    points += 1
    st.write('Correct',name,',good job')
elif Q2 == 'Çhoose your answer':
    st.write('Please choose an answer')
else:
    st.write('Incorrect',name,', try again!')

st.info('Question 3 – Fainting')
st.write('you see your friend faint while standing in the sun ☀️')
st.write('what should you do first?')
Q3 = st.selectbox('Choose the correct question',
                  ['Çhoose your answer','Lay them on their back and lift their legs',' Give them food immediately','Shake them to wake them up'])

if Q3 == 'Lay them on their back and lift their legs':
    points += 1
elif Q3 == 'Çhoose your answer':
    st.write('Please choose an answer')
    st.write('Correct',name,',good work!')
else:
    st.write('Incorrect',name,', try again!')
if st.button('check my answers'):
    if points == 3:
         st.write('you got 3 out of 3 questions right',name,'You know your first aid well.🎉')
         st.balloons()
    elif points == 2:
        st.write('you got 2 out of 3 questions right',name,'Just a little more practice needed.👍')
    elif points == 1:
        st.write('you got 1 out of 3 questions right',name,'keep on trying!👍')
    elif points == 0:
        st.write('you got 0 out of 3 questions right',name,'Keep learning! First aid can save lives.📚')



    

    