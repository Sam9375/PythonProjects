import streamlit as st

#create a dictionary of messi and Ronaldo with the following attributes:
#the country they play for
#the clubs they play for
#how many games played
#how many goals scored
#how many assist made
#then convert to a table
st.subheader('Messi & Ronaldo')
players = {'Player name':['Messi','Ronaldo'],'country':['Argentina','Portugal'],'club':['Argentina national football team','Portugal national football team'],'Games played':[1114,'Over 1,400'],'Assists':[386,268]}
st.write(players)
st.table(players)
