## Prompt --> LLM --> Gemini Pro --> Query --> SQL database --> Response 
## Implementation
## 1) SQLite --> Insert records --> python
## 2) LLM Application --> Gemini Pro --> SQL database

## import necessary libraries
import os
import sqlite3
import streamlit as st
import google.generativeai as genai

## Load the .env file
from dotenv import load_dotenv
load_dotenv()

## Loading the google api key
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question, prompt):
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt, question])
    
    return response.text

## Function to retrieve records from SQL database
def read_sql_query(sql_query, database):
    
    ## Create connection
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    
    ## Close the connection
    connection.commit()
    connection.close()
    
    ## Display the data
    for row in rows:
        print(row)

    return rows

prompt ="""
    You are a MySQL expert. Based on the user's question, generate a syntactically correct MySQL query. 
    Only return the query text, nothing else. Example 1: What is the name and class of the student who scored 92 marks?
    SELECT name, class FROM students WHERE marks = 92; also, the SQL code shouldn't have ```sql ... ``` text or any other text, only the SQL word in output
"""

## Streamlit application
st.set_page_config(page_title = "Gemini Text-to-SQL", page_icon = ":question:")
st.header("Gemini Text-to-SQL Application")

## Input fields
user_question = st.text_input('Input Question:', key = 'input')
submit = st.button('Submit Question')

## When the submit button is clicked
if submit and user_question:
    
    ## Get the response from Gemini LLM
    response = get_gemini_response(user_question, prompt)
    print(response)
    
    ## Get the SQL query from Gemini LLM
    data = read_sql_query(response, 'students.db')
    st.subheader("The SQL query from Gemini LLM is: ")
    
    for row in data:
        print(row)
        st.header(row)

