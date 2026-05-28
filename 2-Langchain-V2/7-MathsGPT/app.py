## Streamlit application to perform math calculations

## Import necessary libraries
import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import LLMMathChain, LLMChain
from langchain_classic.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents import Tool, initialize_agent
from langchain_classic.callbacks import StreamlitCallbackHandler

## Set up the Stramlit app
st.set_page_config(page_title = "Text To Math Problem Solver And Data Search Assistant",page_icon="🧮")
st.title("Text To Math Problem Solver Using Gemma 2")

## Get the API key
groq_api_key = st.sidebar.text_input(label = "Groq API Key", type = "password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

llm = ChatGroq(model = "llama-3.3-70b-versatile", api_key = groq_api_key, temperature=0)

## Initializing the tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name = "Wikipedia",
    func = wikipedia_wrapper.run,
    description = "A tool for searching the internet to find the various information on the topics mentioned"
)

## Initialize the Math tool
math_chain = LLMMathChain.from_llm(llm = llm)
calculator = Tool(
    name = "Calculator",
    func = math_chain.run,
    description = "A tools for answering math related questions. Only input mathematical expression need to bed provided"
)

## Get the prompt for the template
prompt = """
Your a agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question:{question}
Answer:
"""

## Get the prompt template
prompt_template = PromptTemplate(
    input_variables = ["question"],
    template = prompt
)

## Combine all the tools into chain
chain = LLMChain(llm = llm, prompt = prompt_template)

reasoning_tool=Tool(
    name = "Reasoning tool",
    func = chain.run,
    description = "A tool for answering logic-based and reasoning questions."
)

## initialize the agents
assistant_agent = initialize_agent(
    tools = [wikipedia_tool, calculator, reasoning_tool],
    llm = llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = False,
    handle_parsing_errors = True
)

## Initialize the session state and chat history
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a MAth chatbot who can answer all your maths questions"}
    ]

## Let chat history be displayed
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## Let's start the interaction
question = st.text_area("Enter youe question:", "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            ## Create a callback for the LLM response
            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            
            ## Store the response in session state
            st.session_state.messages.append({'role':'assistant', "content":response})
            
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")