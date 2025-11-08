import streamlit as st


st.title('Kids Toy Store')


car, car2, car3 = st.columns(3)
with car:
    st.image('https://m.media-amazon.com/images/I/81pa-dG26dL._AC_UL1600_FMwebp_QL65_.jpg')

with car2:
    st.subheader('Remote Control Car: 45$')

with car3:
    cars = st.number_input('How many cars would you like to buy?',0)
st.divider()

drone1, drone2, drone3 = st.columns(3)
with drone1:
    st.image('https://m.media-amazon.com/images/I/81+byPhlpkL._AC_UL800_FMwebp_QL65_.jpg')

with drone2:
    st.subheader('Drone with camera: 87$')

with drone3:
    drone = st.number_input('How many drones would you like to buy?',0)
st.divider()

ball1, ball2, ball3 = st.columns(3)
with ball1:
    st.image('https://m.media-amazon.com/images/I/81YG8vHgeNL._AC_UL800_FMwebp_QL65_.jpg')

with ball2:
    st.subheader('Hover soccer ball: 36$')

with ball3:
   ball = st.number_input('How many hover balls do you want to buy?',0)
st.divider()

bot1, bot2, bot3 = st.columns(3)
with bot1:
    st.image('https://m.media-amazon.com/images/I/61tLrdxo+9L._AC_UL800_FMwebp_QL65_.jpg')

with bot2:
    st.subheader('Robot toy: 27$')

with bot3:
    bot = st.number_input('how many robots do you want to buy?',0)
st.divider()
lego1, lego2, lego3 = st.columns(3)

with lego1:
    st.image('https://m.media-amazon.com/images/I/81b-29udbRL._AC_UL800_FMwebp_QL65_.jpg')

with lego2:
    st.subheader('Lego Creeper: 30$')

with lego3:
   lego = st.number_input('how many lego sets do you want to buy?',0)
     
# if st.button('Check My Bill'):
#     st.write('Your bill is',bill)