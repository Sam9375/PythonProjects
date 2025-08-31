import streamlit as st
import pandas as pd #this helps to work on CSV files and tables

#Try and except is used to make decisions when there is an error in the code
#try to do this
try:
    scoresfile = pd.read_csv('student_scores.csv') #try to read this file
except:
    scoresfile = pd.DataFrame()
    #if error reading this csv file
    
# A CSV file is used to store text sepearted by commas


menu = st.sidebar.selectbox('menu',['input scores','view database'])

if menu == 'view database':
  st.table(scoresfile)

if menu == 'input scores':
    st.title('Welcome to aspendale school')
    name = st.text_input('please enter your name')
    col1, col2 = st.columns(2)
    with col1:
        mathscore = st.number_input('please enter your math score:',0,100)
        englishscore = st.number_input('please enter your english score:',0,100)
    with col2:
        sciencescore = st.number_input('please enter your science score:',0,100)

        frenchscore = st.number_input('please enter your french score:',0,100)
    totalscore = mathscore + englishscore + sciencescore + frenchscore
    average = totalscore/4
    if st.button('Check My Score'):
        if average >= 90:
            grade = 'A+'
        elif average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        elif average >= 50:
            grade = 'D'
        elif average >= 40:
            grade = 'F'
        st.write(name,'your total score is',totalscore,'and your grade is',grade)

        studentdict = {'Name':[name], 'Math':[mathscore], 'English':[englishscore], 'Science':[sciencescore],
                        'French':[frenchscore], 'Total':[totalscore],'Average':[average], 'Grade':[grade]}

        #st.table(studentdict)
        #st.write(studentdict)
        student_table = pd.DataFrame(studentdict) #convert this dict to a table
        jointables = pd.concat([scoresfile,student_table],ignore_index=True) #join the old table with the new table
        jointables.to_csv('student_scores.csv',index=False)
        #st.table(studentdict)
        st.success('saved')