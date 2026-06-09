import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("Code explainer")
a="Your a code explainer.Explain the given code line by line  other than code if they ask say sorry i cant do that"
prompt=st.text_input("Enter your Requirement:")
if st.button("generate"):
    response = model.generate_content(a+prompt)
    st.write(response.text)
