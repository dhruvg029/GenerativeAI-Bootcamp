import os
import time
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

## Loading the groq and google api keys
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

st.title('Gemma Model Document QnA')

## Loading the Groq LLM model
llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key = groq_api_key,
    temperature = 0
)

prompt = ChatPromptTemplate.from_template("""
Answer the question accurately based on the context provided.
<context>
{context}
</context>
Questions: {input}
""")

## Creating the function to get the vector embeddings and creating the vector store
def vector_embedding():
    if "vector_store" not in st.session_state:

        ## Defining the embedding
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001", google_api_key=os.environ.get("GOOGLE_API_KEY"))
        ## Loading the pdf document
        st.session_state.loader = PyPDFLoader('./sample.pdf')
        st.session_state.docs = st.session_state.loader.load()
        
        ## Splitting the document into chunks
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vector_store = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

## Creating the text input field
prompt1 = st.text_input("Ask a question about the document")

if st.button('Create Vector Store'):
    vector_embedding()
    st.write('Vector Store Created Successfully')

## Creating the document chain and retrieval chain
if prompt1:
    
    ## Creating the document chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    
    ## Creating the retrieval chain
    retrieval_chain = create_retrieval_chain(st.session_state.vector_store.as_retriever(), document_chain)

    time = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    st.subheader('The Response is:')
    st.write(response['answer'])

    ## Displaying the response
    with st.expander("Document similarity search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("_________")
        
