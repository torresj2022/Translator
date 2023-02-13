from deep_translator import GoogleTranslator
import streamlit as st
import pandas as pd
import io

st.write("# Welcome to the file translator")

def translate(x):
    if x != 'None' and x != '.':
        try:
            y = GoogleTranslator(source='auto', target='en').translate(x)
        except:
            y = "did not translate"
        return y
    else:
        return x


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
    file = file.iloc[:1000]
    
    if y:
       
       for i in range(0,len(y)): 
            st.write("Column", y[i],  "is being translated. There are ", len(y[i]), " rows to translate")
            file["translated"+y[i]] = file.apply(lambda x: translate(x[y[i]]), axis = 1)
            ##st.table(file[[y[i],"translated "+y[i]]])
            st.write("Column", y[i],  "translated, it has been saved on column", "translated "+y[i])
       st.write("Success, download your file from the following button")
       buffer = io.BytesIO()
       with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
         # Write each dataframe to a different worksheet.
            file.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            st.download_button(
                    label="Download excel file",
                    data=buffer,
                    file_name="translated_file.xlsx",
                    mime="application/vnd.ms-excel")
