import streamlit as st
import pandas as pd

try:
    gamecsv = pd.read_csv('game.csv')
    
except:
    gamecsv = pd.DataFrame()

st.table(gamecsv)

name = st.text_input('please enter your name')
age = st.number_input('please enter your age')
bestgame = st.text_input('please enter your best game')




if st.button('save information'):
    gamedict = {'name':[name], 'game':[bestgame]}
    gametable = pd.DataFrame(gamedict)
    gametable.to_csv('game.csv',mode='a',index=False,header=gamecsv.empty,)