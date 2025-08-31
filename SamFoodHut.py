import streamlit as st

bill = 0
#meal, drinks, fruits, snacks
st.title('Sam Food Hut')
st.image('https://www.shutterstock.com/shutterstock/photos/1517506040/display_1500/stock-photo-food-collage-of-various-fast-food-meals-and-drinks-1517506040.jpg')
st.subheader('Meal Category')
food1, food2, food3, food4 = st.columns(4)
with food1:
    if st.checkbox('pizza - 15$'):
        st.write('Done!')
        bill +=15
   
with food2:
    if st.checkbox('fish & chips - 10$'):
        st.write('Done!')
        bill +=10
    
with food3:
    if st.checkbox('chicken snitzel - 20$'):
        st.write('Done!')
        bill +=20
with food4:
    if st.checkbox('burger & fries - 25$'):
        st.write('Done!')
        bill +=25
    
st.subheader('Drinks')
drink1, drink2, drink3, drink4 = st.columns(4)
with drink1:
    if st.checkbox('Apple Juice - 5$'):
        st.write('Done!')
        bill +=5
with drink2:
    if st.checkbox('orange soda - 7$'):
        st.write('Done!')
        bill +=7
with drink3:
    if st.checkbox('coca cola - 6$'):
        st.write('Done!')
        bill +=6
with drink4:
    if st.checkbox('Sprite - 4$'):
        st.write('Done!')
        bill  +=4

st.subheader('Fruits')
fruit1, fruit2, fruit3, fruit4 = st.columns(4)
with fruit1:
    if st.checkbox('Orange - 4$'):
     st.write('Done!')
     bill +=4

           
with fruit2:
    if st.checkbox('Apple - 4$'):
            st.write('Done!')
            bill +=4
        
with fruit3:
     if st.checkbox('Mango - 6$'):
            st.write('Done!')
            bill +=6
       
with fruit4:
    if st.checkbox('Pineapple - 8$'):
            st.write('Done!')
            bill +=8
        
st.subheader('Snacks')
snack1, snack2, snack3, snack4 = st.columns(4)
with snack1:
     if st.checkbox('Cheese & Crackers - 10$'):
          st.write('Done!')
          bill +=10
with snack2:
      if st.checkbox('Jelly Cup - 15$'):
          st.write('Done!')
          bill +=15
with snack3:
     if st.checkbox('Cinammon Doughnut - 6$'):
          st.write('Done!')
          bill +=6
with snack4:
     if st.checkbox('Brownie - 3$'):
          st.write('Done!')
          bill +=3

if st.button('Check My Bill'):
        st.write('You bill is',bill,'dollars.')

if st.checkbox('Click to split bill with others'):
    people = st.slider('How many people',1,20)
    payperperson = bill/people
    st.write('Each person will have to pay',payperperson,'dollars')
