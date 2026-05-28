## Simple Generative Q&A Chatbot With Ollama
## Important libraries to install
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

## To generate the response
def generate_response(question, llm, temperature, max_tokens):
    
    ## Get the ollama model
    llm = Ollama(model = llm)
    
    ## Get the output parser
    output_parser = StrOutputParser()
    
    ## Combine the three with the help of chain
    chain = prompt | llm | output_parser
    
    ## Invoke the chain
    answer = chain.invoke({'question':question})
    return answer

## Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")

## Select the OpenAI model
llm = st.sidebar.selectbox("Select Open Source model",["mistral"])

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

## Check if user input is provided
if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")


