import streamlit as st
bill = 0
st.title('Electronics Store')
st.subheader('Home Electronics')
HomeElectronic1, HomeElectronic2, HomeElectronic3 = st.columns(3)
with HomeElectronic1:
    if st.checkbox('Air Conditioner - 200$'):
        st.write('Done!')
        bill += 200
with HomeElectronic2:
    if st.checkbox('Fan - 70$'):
        bill += 70
        st.write('Done!')   
with HomeElectronic3:
    if st.checkbox('Microwave - 65$'):
        st.write('Done!') 
        bill += 65
st.subheader('Office Electronics')
officeelectronic1, officeelectronic2, officeelectronic3 = st.columns(3)
with officeelectronic1:
    if st.checkbox('Heater - 95$'):
        st.write('Done!')
        bill += 95
with officeelectronic2:
    if st.checkbox('Printer - 75$'):
        st.write('Done!')
        bill += 75
with officeelectronic3:
    if st.checkbox('Monitor - 120$'):
        st.write('Done!')
        bill += 120
st.subheader('School Electronics')
schoolelectronic1, schoolelectronic2, schoolelectronic3 = st.columns(3)
with schoolelectronic1:
    if st.checkbox('Projector - 210$'):
        st.write('Done!')
        bill += 210
with schoolelectronic2:
    if st.checkbox('TV - 245$'):
        st.write('Done!')
        bill += 245
with schoolelectronic3:
    if st.checkbox('Calculator - 30$'):
        st.write('Done!')
        bill += 30

if st.button('Check My Bill'):
    st.write('Your bill is',bill,'dollars')