from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd
from googletrans import Translator
import math




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
def create_batches(data, batch_size):
                return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

uploaded_file = st.file_uploader("Please add the csv/excel file to translate")
if uploaded_file is not None:
###x =  st.text_input("Please add file path", value ="", key="text")
    # Can be used wherever a "file-like" object is accepted:
    if '.xls' in uploaded_file.name or '.xlsx' in uploaded_file.name:
        file = pd.read_excel(uploaded_file)
    elif '.csv' in uploaded_file.name:
        file = pd.read_csv(uploaded_file)
    


    columns = file.columns
    y =  st.multiselect('What are the columns to translate',columns)

    file = file.fillna('None')
    file = file
    final = []
    if y and st.button('Translate'):
       
       for i in range(0,len(y)):
            counted_rows = len(file[y[i]])
            st.write("Column", y[i],  "is being translated. There are ", counted_rows , " rows to translate.")
            # Assuming 'dataset' is your data
            batches = create_batches(file, 1000)
            st.write("This file will be processed in {} batches due processing time issues with streamlit".format(len(batches)))
            for number, data in enumerate(batches):
                st.write("processing batch {}".format(number + 1))
                data["translated"+y[i]] = data.apply(lambda x: translate(x[y[i]]), axis = 1)
                final.append(data)
                st.write("Batch {} has been processed".format(number + 1))
            st.write("Column", y[i],  "translated, it has been saved on column", "translated "+y[i])

       st.write("Success, download your file from the following button")
       def convert_df(df):
            return df.to_csv().encode('utf-8')

       final_data = pd.concat(final) 
       csv = convert_df(final_data)

       st.download_button(
            "Download the file",
            csv,
            "translated_file_{}.csv".format(number + 1),
            "text/csv",
            key='browser-data'
                    )
