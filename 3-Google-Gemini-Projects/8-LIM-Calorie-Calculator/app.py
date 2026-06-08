import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

## Loading the environment variables
load_dotenv()

## Loading the google api key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Function to get the gemini response
def get_gemini_response(input_text, image):
    """
    Function to get the response from Gemini LLM
    """
    model = genai.GenerativeModel('gemini-3.5-flash')
    response = model.generate_content([input_text, image[0]])
    return response.text

## Image processing function
def input_image_setup(uploaded_file):
    """
    Function to get the image from the uploaded file
    """
    ## Checking if the file is uploaded
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        ## Converting the bytes data to image parts
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        
        return image_parts
    
    else:
        raise FileNotFoundError('No file uploaded.')
        
## Page configuration
st.set_page_config(page_title = "LIM Calorie Calculator", page_icon = ":spoon: ")
st.title("🍳 Calorie Calculator using Gemini")
st.text("Calculate the calories in your food")

uploaded_file = st.file_uploader('Upload your food image here... ', type = ['png', 'jpg', 'jpeg'])

## Adding the submit button
submit = st.button("Tell me about the calories")
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, width = 400)

input_prompt = """
You are a expert Nutritionist and Dietician.
Your task is to analyze the food image provided by the user and determine the calories of every food item
with calories intake in the format:
    1. Item 1 - no of calories
    2. Item 2 - no of calories
    3. Item 3 - no of calories
    ... 
    
Provide the calorie count in a clear, concise, and easy-to-understand format. You should not share any information that is not related to the food item.
You can also mention whether the food is healthy or not and mention the percentage split of the ratio of nutrients like 
carbohydrates, proteins, fats, etc. And finally give the total calorie intake of the food item.

"""

if submit:
    image_data = input_image_setup(uploaded_file)
    
    ## Getting the response from Gemini LLM
    with st.spinner("Analyzing the food..."):
        response = get_gemini_response(input_prompt, image_data)
    
    st.subheader("The response is: ")
    st.markdown(response)

        
    