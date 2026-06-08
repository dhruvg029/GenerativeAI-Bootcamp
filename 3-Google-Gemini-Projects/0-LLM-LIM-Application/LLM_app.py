## Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

## Load the .env file
load_dotenv()

## Configuration using the google api key
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## Function to load the model and get responses
model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(question):
    """
    Send the user's question to the model and return the response.
    """
    response = model.generate_content(question)
    return response.text

## Inititalize the streamlit application
st.set_page_config(page_title="Ask Gemini AI", page_icon=":star:")
st.header('Gemini LLM Application')

## Creating the input field
input = st.text_input("Enter your question", key = 'input')

## Creating the submit button
submit = st.button('Ask the Question')

## When the submit button is clicked
if submit and input:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)