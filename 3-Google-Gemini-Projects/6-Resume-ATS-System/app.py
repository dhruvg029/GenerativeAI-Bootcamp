## Field to put my JD
## Upload a PDF of my resume
## Button to sumbit
## PDF to image --> processing --> Gemini Pro 
## Prompt Templates (Multiple prompts)

import base64
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import pdf2image
import io

load_dotenv()

## Loading the google api key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Get the Gemini response
def get_gemini_response(input, pdf_content, prompt):
    """
    Function to get the response from Gemini LLM
    """
    model = genai.GenerativeModel('gemini-3.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    """
    Function to convert PDF to image and return the base64 encoded image
    """
    if uploaded_file is not None:
        
        ## convert PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        
        ## Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format = 'JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        
        return pdf_parts
    
    else:
        raise FileNotFoundError("No File Found")
    
## Streamlit application
st.set_page_config(page_title = "Gemini Resume ATS System", page_icon = ":question:")
st.header("Gemini Resume ATS Tracking System")

## Input fields
user_text = st.text_area('Job Description: ', key = 'input')
uploaded_file = st.file_uploader('Upload your PDF here... ', type = ['pdf'])

if uploaded_file is not None:
    st.write('PDF uploaded successfully!')

submit1 = st.button('Can you tell me about the resume?')
submit2 = st.button('What is the percentage match?')

input_prompt1 = """
    You are an experience Technical Human Resource Manager, in the field of any job rule from Data Science or Artificial Intelligence, 
    Big Data Engineering, or DevOps, or Data Analyst or MERN Stack Developer or Full Stack Web Developer. Your task is to evaluate the resume provided by the candidate and determine if 
    they are a good fit for the job description. Analyze the resume and give a detailed summary of the candidate's skills, experience, and qualifications.
    Provide the summary in a clear, concise, and easy-to-understand format. Also share your professional feedback based on your experience as a Technical Human Resource Manager.
    You should not disclose any personal information of the candidate or the company. You should not share any confidential information.
    You should not share any information that is not related to the job description.
"""

input_prompt2 = """
    You are a skilled ATS (Applicant Tracking System) specialist in the field of Data Science or Artificial Intelligence, or
    Big Data Engineering, or DevOps, or Data Analyst or MERN Stack Developer or Full Stack Web Developer. Your task is to compare the candidate's resume with the job descruption and give the percentage match.
    Identify the key skills, technologies, and qualifications mentioned in the job description and compare them with the candidate's resume.
    Provide the analysis in a clear, concise, and easy-to-understand format. Give the You should not disclose any personal information of the candidate or the company. 
    You should not share any confidential information. You should not share any information that is not related to the job description.
"""

## When the submit button is clicked
if submit1:
    if uploaded_file is not None:
        ## Get the pdf content
        pdf_content = input_pdf_setup(uploaded_file)
        
        ## Get the response from Gemini LLM
        response = get_gemini_response(user_text, pdf_content, input_prompt1)
        
        ## Display the response
        st.subheader("The response is: ")
        st.write(response)
    else:
        st.write("Please upload a PDF!")

elif submit2:
    if uploaded_file is not None:
        ## Get the pdf content
        pdf_content = input_pdf_setup(uploaded_file)
        
        ## Get the response from Gemini LLM
        response = get_gemini_response(user_text, pdf_content, input_prompt2)
        
        ## Display the response
        st.subheader("The response is: ")
        st.write(response)
    else:
        st.write("Please upload a PDF!")