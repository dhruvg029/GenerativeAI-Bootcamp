## Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image
import os


## Load the .env file
load_dotenv()

## Configuration using the google api key
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## Function to load the model and get responses
model = genai.GenerativeModel('gemini-3.5-flash')

def get_gemini_response(input, image):
    """
    Send the user's question to the model and return the response.
    """
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## Inititalize the streamlit application
st.set_page_config(page_title = "Gemini Image Demo", page_icon = ":star:")
st.header('Gemini Image Demo')

## Creating the input field
input = st.text_input("Enter your question", key = 'input')

## Creating the upload file button
uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg", "png"])
image = None

## Checking if the file is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded Image', use_container_width = True)

## Creating the submit button
submit = st.button('Tell me about the image')

## When the submit button is clicked
if submit and input:
    response = get_gemini_response(input, image)
    st.subheader('The response is')
    st.write(response)