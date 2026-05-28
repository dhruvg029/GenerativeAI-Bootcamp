## Streamlit application to perform text summarization on YT or Website URL

## Import necessary libraries
import validators, streamlit as st
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

## Streamlit app
st.set_page_config(page_title = "LangChain: Summarize Text From YT or Website", page_icon = "🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

## Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type = "password")

## Get the website or YT url to be summarized
generic_url = st.text_input("URL", label_visibility = "collapsed")

## We initialize the LLM with the API key and model name
llm = ChatGroq(model = "llama-3.3-70b-versatile", api_key = groq_api_key, temperature = 0)

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""

## Get the prompt to be provided to the LLM
prompt = PromptTemplate(template = prompt_template, input_variables = ["text"])

## Check if the user has clicked the button to summarize
if st.button("Summarize the Content from YT or Website"):
    
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    
    elif not validators.url(generic_url):
        st.error("Please enter a valid url. It can may be a YT video url or website url")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if 'youtube.com' in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info = True)
                else:
                    loader = UnstructuredURLLoader(urls = [generic_url], ssl_verify = False,
                                                 headers = {
                                                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                                                })
                docs = loader.load()

                ## Chain For Summarization
                chain = load_summarize_chain(llm, chain_type = "stuff", prompt = prompt)
                output_summary = chain.run(docs)
                
                ## Showing the final summary
                st.success(output_summary)
                
        except Exception as e:
            st.exception(f"Exception:{e}")
                    