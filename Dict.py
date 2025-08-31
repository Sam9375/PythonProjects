import streamlit as st

#a list is used used to store more than one pieces of data
#a dictionary is used to store multiple data in categories

#storing single data/item in a category
storeproduct = ('units - 4','price - 4','dicount - 10% off','sold - 3')

#storing multiple data/item in a category
storeproduct = {'units':[4],'price':[30],'discount':['10% off'],'sold':[3]}

st.table(storeproduct)
st.write(storeproduct)