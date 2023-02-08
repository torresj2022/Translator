from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd
from io import StringIO

def translate(x):
    if x != 'None':
        try:
            y = GoogleTranslator(source='auto', target='en').translate(x)
        except:
            y = "did not translate"
        return y
    else:
        return x

uploaded_file = st.file_uploader("Please add the excel file to translate")
if uploaded_file is not None:
###x =  st.text_input("Please add file path", value ="", key="text")
    # Can be used wherever a "file-like" object is accepted:
    file = pd.read_excel(uploaded_file)
    

###if x != '':
    ##file = pd.read_excel(x)
    columns = file.columns
    y =  st.multiselect(
    'What are the columns to translate',
    columns)
    #file = pd.read_excel(x)
    file = file.fillna('None')
    file = file.iloc[:100]
    if y: 
       for i in range(0,len(y)): 
            file["translation"+y[i]] = file.apply(lambda x: translate(x[y[i]]), axis = 1)
       st.table(file[[y[i], "translation"+y[i]]])
