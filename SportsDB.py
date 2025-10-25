import streamlit as st
import pandas as pd
name = st.text_input('Please enter your name: ')
col1, col2 = st.columns(2)
filelink = 'sportfile.csv'
try:
    filelink = pd.read_csv(filelink)

except:
     sportfile = pd.DataFrame()


with col1:
    sprint = st.number_input('Please enter your score for the 100m sprint: ')
    longjump = st.number_input('Please enter your score for the long jump: ')

with col2:
    shotput = st.number_input('Please enter your score for the shot put: ')
    highjump = st.number_input('Please enter your score for the high jump: ')

totalscore = sprint + longjump + shotput + highjump
average = totalscore/4

if average >= 90:
    PL = 'A+'

elif average >= 80:
    PL = 'A'

elif average >= 70:
    PL = 'B'

elif average >= 60:
    PL = 'C'

elif average >= 50:
    PL = 'D'

elif average <= 50:
    PL = 'F'

if st.button('submit student sport info'):
    sportdict = {'Name':[name], 'Sprint':[sprint],
                  'Long Jump':[longjump],
                    'Shotput':[shotput], 'High Jump':[highjump] }
    
    sporttable = pd.DataFrame(sportdict)
    sporttable.to_csv(filelink,mode='a',header=sportfile.empty,index=False)
    st.success('Student Score Saved!')