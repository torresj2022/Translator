from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd
from io import StringIO

st.write("# Welcome to the file translator")
def translate(x):
    if x != 'None':
        try:
            y = GoogleTranslator(source='auto', target='en').translate(x)
        except:
            y = "did not translate"
        return y
    else:
        return x
       
def excel_file(df):
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.close()

uploaded_file = st.file_uploader("Please add the csv/excel file to translate")
if uploaded_file is not None:
###x =  st.text_input("Please add file path", value ="", key="text")
    # Can be used wherever a "file-like" object is accepted:
    if 'xls' in uploaded_file.name:
        file = pd.read_excel(uploaded_file)
    if 'csv' in uploaded_file.name:
        file = pd.read_csv(uploaded_file)
    

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
            file["translated"+y[i]] = file.apply(lambda x: translate(x[y[i]]), axis = 1)
            ##st.table(file[[y[i],"translated"+y[i]]])
   

       excel = file.to_excel()

       st.download_button(
        label="Download data as excel",
        data=excel,
        file_name='translation.xlsx',
        mime="application/vnd.ms-excel",
        )
