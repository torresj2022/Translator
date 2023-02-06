from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd

def translate(x):
    try:
        y = GoogleTranslator(source='auto', target='en').translate(x)
    except:
        y = "did not translate"
    return y
x =  st.text_input("Please add file path", value ="", key="text")


if x != '':
    file = pd.read_excel(x)
    columns = file.columns
    y =  st.multiselect(
    'What are the columns to translate',
    columns)
    file = pd.read_excel(x)
    file = file.fillna('None')
    if y: 
        for i in range(0,len(y)): 
            file["translation"+y[i]] = file.apply(lambda x: translate(x[y[i]]), axis = 1)
            st.table(file["translation"+y[i]])
