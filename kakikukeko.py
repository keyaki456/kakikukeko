import streamlit as st
import markovify
from googletrans import Translator

translator = Translator()

st.write("MtGのフレーバーテキストをマルコフ連鎖でﾓﾁｮﾓﾁｮして新しいフレーバーテキストを作ってgoogle翻訳で日本語にする")

with open("merosu.txt") as f:
    text = f.read()
    text_model = markovify.Text(text)
for a in range(10):
    texten = text_model.make_sentence()
    textja = translator.translate(texten, dest="ja").text
    st.write("~~")
    st.write(texten)
    st.write(textja)