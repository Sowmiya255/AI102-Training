import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("Chatbot")
prompt=st.text_input("Enter your Requirement:")
if st.button("generate"):
    response = model.generate_content(prompt)
    st.write(response.text)


