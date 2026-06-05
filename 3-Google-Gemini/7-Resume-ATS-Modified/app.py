## PDF --> Text using PyPDF2 --> LLM API --> Response

import base64
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import PyPDF2 as pdf

## Loading the environment variables
load_dotenv()

## Loading the google api key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Function to get the gemini response
def get_gemini_response(input_text):
    """
    Function to get the response from Gemini LLM
    """
    model = genai.GenerativeModel('gemini-3.5-flash')
    response = model.generate_content(input_text)
    return response.text

## Get the text from the PDF
def get_pdf_text(pdf_file):
    """
    Function to get the text from the PDF
    """
    pdf_reader = pdf.PdfReader(pdf_file)
    text = ""

    ## Iterate through all the pages and extract the text
    for page in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page]

        text += str(page.extract_text())

    return text

input_prompt = """
Act like a skilled or very experienced ATS (Applicant Tracking System) Specialist and Human Resource Manager in the field of
software engineering, data science, data analytics, cloud computing,DevOps, Blockchain, Machine Learning, Artificial Intelligence, MERN Stack Developer, or Full Stack Web Developer.
Your task is to analyze the resume provided by the candidate and determine if they are a good fit for the job description. 
Analyze the resume and give a detailed summary of the candidate's skills, experience, and qualifications. Provide the summary in a clear, concise, and easy-to-understand format.

Provide your professional feedback based on your experience as a Technical Human Resource Manager.

You should not disclose any personal information of the candidate or the company. You should not share any confidential information. 
You should not share any information that is not related to the job description.

Resume: {text}
Job Description: {jd}

I want the response in one single string having the structure
{{"JD Match": "%", "MissingKeywords:[]", "Profile Summary":""}}
"""

st.title("AI Resume ATS System")
st.text('Improve your resume ATS')
st.text_area('Enter Job Description', key = "input", height = 250)

## Adding the button
submit = st.button('Submit')

uploaded_file = st.file_uploader("Upload your PDF here... ", type = ['pdf'])

if uploaded_file is not None:
    st.write('PDF uploaded successfully!')
    
    ## Get the text from the PDF
    pdf_text = get_pdf_text(uploaded_file)
    
    ## Get the response from Gemini LLM
    response = get_gemini_response(input_prompt)
    
    ## Display the response
    st.subheader("The response is: ")
    st.write(response)
