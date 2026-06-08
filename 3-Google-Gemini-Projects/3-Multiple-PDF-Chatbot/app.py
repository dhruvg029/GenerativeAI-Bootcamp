import langchain_classic
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_classic.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_classic.prompts import PromptTemplate
from PyPDF2 import PdfReader
import google.generativeai as genai
import streamlit as st
import os

## Load the .env file
load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))



## Fetch the PDF text from the uploaded PDF files
def get_pdf_text(pdf_docs):
    """
    Extract text from multiple PDF files.
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

## Splitting the text into smaller chunks
def get_text_chunks(text):
    """
    Split text into smaller chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 1000)
    chunks = text_splitter.split_text(text)
    return chunks

## Create embeddings for the text chunks
def get_vector_store(text_chunks):
    """
    Create vector store from text chunks.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

    ## Create the vector store from the text chunks
    vector_store = FAISS.from_texts(text_chunks, embedding = embeddings)

    ## Save the vector store locally
    vector_store.save_local('faiss_index')

## Get the conversational chain
def get_conversational_chain():
    """
    Create a conversational chain.
    """
    prompt_template = """
    You are an AI assistant that can answer questions based on the context provided.
    Here is the context:
    {context}
    Here is the question:
    {question}
    Answer the question as detailed as possible based on the context.
    If the answer is not in the context, say that you don't know, but don't give the wrong answer.
    """
    ## Load the model
    model = ChatGoogleGenerativeAI('gemini-3.5-flash')

    ## Get the prompt template
    prompt = PromptTemplate(template = prompt_template, input_variables = ['context', 'question'])

    ## Create the chain
    chain = load_qa_chain(model, chain_type = 'stuff', prompt = prompt)
    
    return chain

def handle_user_input(user_question):
    """
    Handle the user's input.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")

    ## Get the vector store
    new_db = FAISS.load_local('faiss_index', embeddings, allow_dangerous_deserialization=True)

    ## Get the documents
    docs = new_db.similarity_search(user_question)

    ## Get the conversational chain
    chain = get_conversational_chain()

    ## Get the response from the model
    response = chain({
        'input_documents': docs, 'question': user_question
        }, return_only_outputs = True
    )

    ## Display the response
    st.write('Response: ', response['output_text'])

def main():
    st.set_page_config(page_title = "Multiple PDF Chatbot", page_icon = ":star:")
    st.header('Multiple PDF Chatbot')

    ## Creating the input field
    user_question = st.text_input("Ask a question about your documents: ", key = 'input')

    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.title('Menu:')
        pdf_docs = st.file_uploader('Choose PDFs', type = ['pdf'], accept_multiple_files = True)
        
        ## Checking if the PDF files are uploaded
        if st.button('Submit & Process'):
            
            ## Showing the spinner while processing
            with st.spinner('Processing...'):
                
                ## Get the PDF text
                text = get_pdf_text(pdf_docs)
                
                ## Get the text chunks
                text_chunks = get_text_chunks(text)
                
                ## Create the vector store
                get_vector_store(text_chunks)
                st.success('Done!')

if __name__ == '__main__':
    main()