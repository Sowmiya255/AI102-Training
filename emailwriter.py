import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("Email writer")
a="Your an email writer.write an email based on their requirement other then email they ask say sorry i cant do that"
prompt=st.text_input("Enter your Requirement:")
if st.button("generate"):
    response = model.generate_content(a+prompt)
    st.write(response.text)
