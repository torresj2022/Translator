from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd
st.text_input("text to translate", key="text")

def translate(x):
    try:
        y = GoogleTranslator(source='auto', target='en').translate(x)
    except:
        y = "did not translate"
    return y
 
translate(text)
