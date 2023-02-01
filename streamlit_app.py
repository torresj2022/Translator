!pip install -U deep-translator
from deep_translator import GoogleTranslator
import pandas as pd
file = pd.read_excel("LATAM.xlsx")
file = file.fillna('None')
def translate(x):
    try:
        y = GoogleTranslator(source='auto', target='en').translate(x)
    except:
        y = "did not translate"
    return y
file['translated'] = file['Q2'].apply(lambda x: translate(x)) 
file['translatedQ3'] = file['Q3'].apply(lambda x: translate(x))
file.to_excel("translation.xlsx")
