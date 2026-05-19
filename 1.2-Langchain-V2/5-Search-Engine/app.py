## This simple generative ai helps to look up information from websites like arxiv, wikipedia or duck duck go, instead of just guessing
## It takes help of tools and agents to find the information and provide it to the user

## Import important libraries
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_classic.agents import initialize_agent, AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler

## Arxiv and wikipedia Tools
## Provide the top result only and restrict the content to 200 characters
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)

## Create tools of arxiv, wikipedia and duckduckgo
arxiv = ArxivQueryRun(api_wrapper = arxiv_wrapper)
wiki = WikipediaQueryRun(api_wrapper = wiki_wrapper)
search = DuckDuckGoSearchRun(name = "Search")

st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

## Chat History
## Logic to preserve chat history, we use st.session_state
## If not, it initializes it with a default greeting from the assistant.
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"assistant", "content": "Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]

## Display chat history
## loop iterates through the saved history and draws the chat bubbles 
## (st.chat_message) on the screen so you can see the ongoing conversation.
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## User prompt and LLM initialization
if prompt := st.chat_input(placeholder = "What is machine learning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    ## We initialize the LLM with the API key and model name
    llm = ChatGroq(
        model = "llama-3.3-70b-versatile",
        api_key = api_key,
        temperature = 0
    )
    
    ## Combine the tools
    tools = [search, arxiv, wiki]
    search_agent = initialize_agent(

        tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        
        ## tells the framework to gently correct the agent
        ## accidentally outputs a tool request in the wrong format
        handling_parsing_errors = True
    )

    with st.chat_message("assistant"):

        ## When the agent decides to search Wikipedia or DuckDuckGo
        ## this handler catches that "thought process" and displays it in a neat, expandable UI box on the Streamlit app.
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts = False)
        
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant', "content":response})
        
        ## write the response
        st.write(response)

