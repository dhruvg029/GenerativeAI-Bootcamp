# 🧠 Generative AI Repertoire
*A curated ledger of Generative AI concepts, frameworks, and production-ready workflows.*

![Hero Banner](https://github.com/user-attachments/assets/fd6eb936-8eb5-47a7-a079-261af01aee63)

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)](#)

</div>

This repository contains implementations of Generative AI concepts and workflows, following courses by [Krish Naik](https://www.krishnaik.in/) on Udemy. It serves as a personal learning ledger and reference guide, and it will be updated continuously as new tools and frameworks emerge. It also consists of recent developments and changes to the Langchain framework, and the code which are in the courses and here, may vary. **Feel free to star it if you find it useful!** ⭐ 

---

## ⚙️ Requirements & Setup

To explore these projects, you need a solid understanding of Python and an enthusiasm for Generative AI terminology. 

**Environment Setup:**
It is highly recommended to use an isolated virtual environment.

```bash
## Clone the repository
git clone "https://github.com/your-username/GenerativeAI-Bootcamp.git"
cd GenerativeAI-Bootcamp

## Create and activate a virtual environment (Python 3.11.x or 3.12.x)
conda create -n venv python=3.11.x
conda activate venv

## Install the dependencies
pip install -r requirements.txt
```

## 📂 Repository Structure

### 🦜 1) Langchain

The langchain framework in this repository is split into two primary segments to demonstrate the transition from legacy LangChain syntax to the modern ecosystem. These resources are from Udemy's [Complete Generative AI Course With Langchain and Huggingface](https://www.udemy.com/course/complete-generative-ai-course-with-langchain-and-huggingface/learn/lecture/44782435?start=150#overview) course.

- [Langchain-V1:](https://github.com/dhruvg029/GenerativeAI-Bootcamp/tree/main/1-Langchain-V1) Legacy implementations and foundational concepts of Langchain which includes basic RAG concepts, retreivers, LCEL and a basic chatbot implementation from scratch.
  - **Introduction:** A simple step by step implementation of a RAG is implemented. From `Data Ingestion` to create `vector stores`, this folder consists of practical examples to illustrate the theory.
  - **LangChain Expression Language:** It allows to easily connect and combine different AI components (like `prompts, language models, tools, and output parsers`) to build complex AI applications.
  - To save history of messages, notebook has been implemented with the usage of `RunnableWithMessageHistory`, `SystemMessage`, `HumanMessage` etc.
  - Vector stores like `Chroma` and `FAISS` are designed to support retrieval of data from (vector) databases and other sources for integration with LLM workflows.
- [Langchain-V2;](https://github.com/dhruvg029/GenerativeAI-Bootcamp/tree/main/2-Langchain-V2) Modern LangChain architecture and production-ready tools such as tools, agents, wrappers, and deployment using streamlit cloud, and some advanced projects with the help of GROQ and OLLAMA models. 
  - **QnA Chatbots:** Some basic chatbots such as a `Conversational RAG`, `Document Search RAG`, and `Chatbot with SQL Toolkit` have been implemented using tools, agents and langchain framework.
  - **LLM Search Engine:** This simple generative ai helps to look up information from websites like `Arxiv`, `wikipedia` or `duck duck go`, instead of just guessing. It takes help of tools and agents to find the information and provide it to the user.
  - **Text Summarization:** A streamlit application to perform text summarization on YT or Website URL. Various inbuilt summarization tools such as `load_summarize_chain()`, `LLMchain()`, and `PromptTemplate()` have been used for experimenting purposes.
  - **MathsGPT:** A streamlit application to perform math calculations using `LLMMathChain()` and `StreamlitCallbackHandler()` functions.
  - A simple project to perform integration of Huggingface with Langchain, using `HuggingFaceEndpoint()`. The difference is to provide the repo id with the token to invoke the LLM.
  - A simple **PDF-Query RAG** to store the data into AstraDB (Cassandra) using `cassIO`, `OllamaEmbeddings` and AstraDB credentials such as `ASTRA_DB_APPLICATION_TOKEN` and `ASTRA_DB_ID`.
  - A CodeLlama assistant implementation using `Gradio` library and rest API.
  - **Hybrid Search:** A simple implementation of Hybrid Search is covered using Langchain and `Pinecone` database, and `PineconeHybridSearchRetriever`.
  - **Graph Databases:** Where Knowledge graph is applied with the help of different tools such as `Neo4jGraph`, created chains with the help of `GraphCypherQAChain` and understand cypher query language with the help of Neo4j AurDB database and instances.
  - **Fine Tuning LLMs:** A simple notebook to demonstrate fine tuning using `LORA`, `QLORA` and `Quantization` methods is created, and `Lamini API` is used to get deep dive knowledge. ]
  - **LangGraph:** Implementation of RAGs and Chatbots using `LangGraph`, and build graphs using `StateGraph()` class, wherein you can add nodes, edges and tools altogether. 

---

### ✨ 2) Google Gemini

This part consists of different projects created with the help of Gemini open source models. The idea is to use them using the `google.generativeai` library, and configure using the `GOOGLE_API_KEY`. These resources are from Udemy's [Building Gen AI App 12+ Hands-on Projects with Gemini Pro](https://www.udemy.com/course/building-gen-ai-app-end-to-end-projects-with-gemini-pro) course.

- **LIM-LLM Application:** Simple streamlit applications using Gemini models such as `Gemini-3.5-Flash` and `Gemini-2.5-Flash` to chat with the LLM, or analyse images with LIM.
- **Conversational Chatbot:** A chatbot application to chat with an open source LLM, and save chat history simultaneously using `Gemini-2.5-flash` model. 
