from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image
import os

## Load the environment variables
load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## Function to load the model and get the response
model = genai.GenerativeModel('gemini-3.5-flash')

def get_gemini_response(input, image, prompt):
    """
    Send the user's question to the model and return the response.
    """
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    """
    Setup the uploaded file for the model.
    """
    if uploaded_file is not None:

        ## Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        ## Create the image parts
        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data': bytes_data
            }
        ]
        return image_parts
    return None

## Set the streamlit application
st.set_page_config(page_title = "Multilanguage Invoice Extractor", page_icon = ":star:")

## Create the title
st.header('Multilanguage Invoice Extractor')

## Create the input field
input = st.text_input('Input: ', key = 'input')

## Create the upload file button
uploaded_file = st.file_uploader('Choose an image...', type = ['jpg', 'jpeg', 'png'])
image = None

## Checking if the file is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded Image', use_container_width = True)

## Creating the submit button
submit = st.button('Tell me about the invoice!')

## Get the input prompt
input_prompt = """
You are an expert in analyzing invoices. We will upload an image of an invoice and based on the input given by the user,
answer the questions asked by the user. If the question is out of scope, please inform the user accordingly.
"""

if submit:

    ## Get the image details
    image_data = input_image_details(uploaded_file)
    
    ## Get the response from the model
    response = get_gemini_response(input, image_data, input_prompt)
    
    ## Display the response
    st.subheader('The response is')
    st.write(response)