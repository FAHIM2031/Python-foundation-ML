from google import genai
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

def convert_text(input_text):
    prompt="convert the text into professional in one line about "+input_text
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text
api_key=os.environ.get("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)

st.title("convert the normal text into professional")
input_text=st.text_area("Enter your text here",placeholder="Enter your text here")
click=st.button("Convert")
if click:
    result=convert_text(input_text)
    st.markdown(f"Professional Text= {result}")
