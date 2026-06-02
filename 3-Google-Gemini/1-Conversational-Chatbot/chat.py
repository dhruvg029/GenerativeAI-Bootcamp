from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import os

## Load the .env file
load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## Load the model
model = genai.GenerativeModel('gemini-2.5-flash')

## Function to get responses and load the model
chat = model.start_chat(history = [])

def get_gemini_response(question):
    """
    Send the user's question to the model and return the response.
    """
    response = chat.send_message(question, stream = True)
    return response

## Inititalize the streamlit application
st.set_page_config(page_title = "Gemini Chatbot", page_icon = ":star:")
st.header('Gemini Conversational LLM Applicaton')

## Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

## Creating the input field
user_input = st.text_input("Input: ", key = 'input')

## Creating the submit button
submit = st.button('Ask the question!')

## When the submit button is clicked
if submit and user_input:
    
    response = get_gemini_response(user_input)

    ## Display the chat history
    st.session_state['chat_history'].append(('You', user_input))

    st.subheader('The response is:')

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot', chunk.text))

st.subheader('Chat History:')

## Display the chat history
for role, message in st.session_state['chat_history']:
    st.write(f"**{role}:** {message}")