import streamlit as st
import markovify
#import MeCab

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

options = st.multiselect('What are your favorite colors',
['Green', 'Yellow', 'Red', 'Blue', 'black', 'orange'],
['Yellow', 'Red'])

st.write('You selectedee:', options)

st.map()

with open("merosu.txt") as f:
    text = f.read()
    text_model = markovify.Text(text, state_size=3)
for a in range(10):
    st.write(text_model.make_sentence())