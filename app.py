import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator")

text = st.text_area("Enter Text to Convert:")
languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Marathi": "mr",
    "Urdu": "ur"
}
dst = st.selectbox("Select Destination Language", list(languages.keys()))
if st.button("Translate"):
    gt = GoogleTranslator(source='en', target=languages[dst])
    result = gt.translate(text)
    st.info(text)
    st.success(result)