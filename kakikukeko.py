import streamlit as st
import markovify
from googletrans import Translator

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
    text_model = markovify.Text(text)
for a in range(10):
    st.write(text_model.make_sentence())

st.write("ああああ")

translator = Translator()
text_en = text_model.make_sentence()
text_ja = translator.translate(text_en, src='en', dest='ja').text

print(text_ja) 