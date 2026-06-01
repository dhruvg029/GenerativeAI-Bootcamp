# 🧠 Generative AI Repertoire

<p align="center">
  <img width="920" height="400" alt="image" src="https://github.com/user-attachments/assets/fd6eb936-8eb5-47a7-a079-261af01aee63" />
</p>

This repository contains implementations of Generative AI concepts and workflows, following courses by [Krish Naik](https://www.krishnaik.in/) on Udemy. It serves as a personal learning ledger and reference guide, and it will be updated continuously as new tools and frameworks emerge. It also consists of recent developments and changes to the Langchain framework, and the code which are in the courses and here, may vary. **Feel free to star it if you find it useful!** ⭐

---

## 📂 Repository Structure

### 1) Langchain

The project is split into two primary segments to demonstrate the transition from legacy LangChain syntax to the modern ecosystem. These resources are from Udemy's [Complete Generative AI Course With Langchain and Huggingface](https://www.udemy.com/course/complete-generative-ai-course-with-langchain-and-huggingface/learn/lecture/44782435?start=150#overview) course.

- [Langchain-V1:](https://github.com/dhruvg029/GenerativeAI-Bootcamp/tree/main/1-Langchain-V1) Legacy implementations and foundational concepts of Langchain which includes basic RAG concepts, retreivers, LCEL and a basic chatbot implementation from scratch.
  - **INTRODUCTION:** A simple step by step implementation of a RAG is implemented. From `Data Ingestion` to create `vector stores`, this folder consists of practical examples to illustrate the theory.
  - **LANGCHAIN EXPRESSION LANGUAGE:** It allows to easily connect and combine different AI components (like `prompts, language models, tools, and output parsers`) to build complex AI applications.
  - To save history of messages, notebook has been implemented with the usage of `RunnableWithMessageHistory`, `SystemMessage`, `HumanMessage` etc.
  - Vector stores like `Chroma` and `FAISS` are designed to support retrieval of data from (vector) databases and other sources for integration with LLM workflows.
- [Langchain-V2;](https://github.com/dhruvg029/GenerativeAI-Bootcamp/tree/main/2-Langchain-V2) Modern LangChain architecture and production-ready tools such as tools, agents, wrappers, and deployment using streamlit cloud, and some advanced projects with the help of GROQ and OLLAMA models. 
  - **QnA CHATBOTS:** Some basic chatbots such as a `Conversational RAG`, `Document Search RAG`, and `Chatbot with SQL Toolkit` have been implemented using tools, agents and langchain framework.
  - **LLM SEARCH ENGINE:** This simple generative ai helps to look up information from websites like `Arxiv`, `wikipedia` or `duck duck go`, instead of just guessing. It takes help of tools and agents to find the information and provide it to the user.
  - **TEXT SUMMARIZATION:** A streamlit application to perform text summarization on YT or Website URL. Various inbuilt summarization tools such as `load_summarize_chain()`, `LLMchain()`, and `PromptTemplate()` have been used for experimenting purposes.
  - **MATHS GPT:** A streamlit application to perform math calculations using `LLMMathChain()` and `StreamlitCallbackHandler()` functions.
  - A simple project to perform integration of Huggingface with Langchain, using `HuggingFaceEndpoint()`. The difference is to provide the repo id with the token to invoke the LLM.
  - A simple **PDF-Query RAG** to store the data into AstraDB (Cassandra) using `cassIO`, `OllamaEmbeddings` and AstraDB credentials such as `ASTRA_DB_APPLICATION_TOKEN` and `ASTRA_DB_ID`.
  - A CodeLlama assistant implementation using `Gradio` library and rest API.
  - **HYBRID SEARCH:** A simple implementation of Hybrid Search is covered using Langchain and `Pinecone` database, and `PineconeHybridSearchRetriever`.
  - **GRAPH DATABASES:** Where Knowledge graph is applied with the help of different tools such as `Neo4jGraph`, created chains with the help of `GraphCypherQAChain` and understand cypher query language with the help of Neo4j AurDB database and instances.
  - **FINE TUNING LLMs:** A simple notebook to demonstrate fine tuning using `LORA`, `QLORA` and `Quantization` methods is created, and `Lamini API` is used to get deep dive knowledge. ]
  - **LANGGRAPH:** Implementation of RAGs and Chatbots using `LangGraph`, and build graphs using `StateGraph()` class. 
