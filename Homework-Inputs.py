import streamlit as st
st.title('Sams Ultimate Quiz!')
st.image('data:image/jpeg;base64,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')
name = st.text_input('Please enter your name: ')
Q1 = st.number_input('First question: whats 5x5?',0)
Q2 = st.number_input('Second question: whats 10 + 10?',0)
Q3 = st.number_input('Third question, how many sides does a triangle have?',0)
Q4 = st.number_input('Fourth question: whats 20 - 6',0)
Q5 = st.text_input('Fifth question: what animals meows?')
Q6 = st.number_input('Sixth question: how many legs does a spider have?',0)
Q7 = st.text_input('Seventh question: what do you call a baby dog?')
Q8 = st.number_input('First question: whats 30 + 30?',0)
Q9 = st.number_input('First question: whats 50 - 20?',0)
Q10 = st.number_input('First question: whats 40 -20?',0)
if st.button('Check answers'):
    st.subheader('Here are your results:')
    if Q1 == 25:
        st.write('Question 1 is Correct!')
    else:
        st.write('Question 1 is Incorrect')

    if Q2 == 20:
        st.write('Question 2 is Correct!')
    else:
        st.write('Question 2 is Incorrect')

    if Q3 == 3:
            st.write('Question 3 is Correct!')
    else:
          st.write('Question 3 is Incorrect')
    
    if Q4 == 14:
            st.write('Question 4 is Correct!')
    else:
          st.write('Question 4 is Incorrect')
    
    if Q5 == 'cat':
            st.write('Question 5 is Correct!')
    else:
          st.write('Question 5 is Incorrect')
    
    if Q6 == 8:
            st.write('Question 6 is Correct!')
    else:
          st.write('Question 6 is Incorrect')
    
    if Q7 == 'puppy':
            st.write('Question 7 is Correct!')
    else:
          st.write('Question 7 is Incorrect')
      
    if Q8 == 60:
            st.write('Question 8 is Correct!')
    else:
          st.write('Question 8 is Incorrect')
    
    if Q9 == 30:
            st.write('Question 9 is Correct!')
    else:
          st.write('Question 9 is Incorrect')
    
    if Q10 == 20:
            st.write('Question 10 is Correct!')
    else:
          st.write('Question 10 is Incorrect')

    st.write('Great job',name,'you did well!')
    