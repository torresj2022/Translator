from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd
from googletrans import Translator




st.write("# Welcome to the file translator")

def translate(x):
    if x != 'None' and x != '.':
        try:
            y = GoogleTranslator(source='auto', target='en').translate(x)
            return y
        except:
                try:
                    y = Translator.translate(text).text
                    return y
                except:
                    y = "did not translate"
                    return y
            
    else:
        return x


uploaded_file = st.file_uploader("Please add the csv/excel file to translate")
if uploaded_file is not None:
###x =  st.text_input("Please add file path", value ="", key="text")
    # Can be used wherever a "file-like" object is accepted:
    if '.xls' in uploaded_file.name or '.xlsx' in uploaded_file.name:
        file = pd.read_excel(uploaded_file)
    elif '.csv' in uploaded_file.name:
        file = pd.read_csv(uploaded_file)
    


    columns = file.columns
    y =  st.multiselect(
    'What are the columns to translate',columns)

    file = file.fillna('None')
    file = file
    
    if y and st.button('Translate'):
       
       for i in range(0,len(y)):
            counted_rows = len(file[y[i]])
            st.write("Column", y[i],  "is being translated. There are ", counted_rows , " rows to translate.")
            
            file["translated"+y[i]] = file.apply(lambda x: translate(x[y[i]]), axis = 1)
            ##st.table(file[[y[i],"translated "+y[i]]])
       
            st.write("Column", y[i],  "translated, it has been saved on column", "translated "+y[i])
       st.write("Success, download your file from the following button")
       def convert_df(df):
           return df.to_csv().encode('utf-8')


       csv = convert_df(file)

       st.download_button(
            "Download the file",
            csv,
            "translated_file.csv",
            "text/csv",
            key='browser-data'
            )
