import streamlit as st

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

options = st.multiselect(
'What are your favorite colors',
['Green', 'Yellow', 'Red', 'Blue', 'black', 'orange'],
['Yellow', 'Red'])

st.write('You selected:', options)