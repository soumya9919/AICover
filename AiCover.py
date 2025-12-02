import streamlit as st
import google.generativeai as genai
import request

genai.configure(api_key=st.secret["GOOGLE_API_KEY"])

st.title("AI COVER GENERATOR")

Job_Title=st.text_input("Enter Job Title: ")
Resume_Summary=st.text_input("Enter Resume Summary: ")

if st.button("Generate Cover Letter"):
    prompt=f"Create a cover letter for {Job_Title} using these resume point:\n {Resume_Summary}"
    
    model=google.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content(prompt)

    st.write(response.text)