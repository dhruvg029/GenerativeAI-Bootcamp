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

#### 🧱 [Langchain-V1](https://github.com/dhruvg029/GenerativeAI-Bootcamp/tree/main/1-Langchain-V1): Foundational Concepts
Legacy implementations and foundational concepts of Langchain including basic RAG concepts, retrievers, LCEL, and chatbots from scratch.

| <div align="center">📂 Concept<img width="175"/></div> | <div align="center">📝 Description<img width="600"/></div> |
| :--- | :--- |
| **📖 RAG Introduction** | Step-by-step implementation of RAG from data ingestion to vector stores. |
| **🔗 LCEL Architecture** | Easily connect components to build complex AI applications. <br><sub>*Tech:* <kbd>Prompts</kbd> <kbd>Language Models</kbd> <kbd>Output Parsers</kbd></sub> |
| **💬 Message History** | Save and manage conversational context dynamically. <br><sub>*Tech:* <kbd>RunnableWithMessageHistory</kbd> <kbd>SystemMessage</kbd></sub> |
| **🗄️ Vector Stores** | Integrate and retrieve data from databases for LLM workflows. <br><sub>*Tech:* <kbd>Chroma</kbd> <kbd>FAISS</kbd></sub> |

<br>

#### 🚀 [Langchain-V2](https://github.com/dhruvg029/GenerativeAI-Bootcamp/tree/main/2-Langchain-V2): Modern & Production-Ready
Modern LangChain architecture, production-ready agents, Streamlit deployments, and advanced projects using GROQ and OLLAMA.

| <div align="center">⚡ Project<img width="175"/></div> | <div align="center">💡 Description<img width="600"/></div> |
| :--- | :--- |
| **🤖 QnA Chatbots** | Conversational RAG, Document Search, and SQL-based chatbots. <br><sub>*Tech:* <kbd>Agents</kbd> <kbd>SQL Toolkit</kbd></sub> |
| **🔍 LLM Search Engine** | Agentic lookup for live web information instead of LLM guessing. <br><sub>*Tech:* <kbd>Arxiv</kbd> <kbd>Wikipedia</kbd> <kbd>DuckDuckGo</kbd></sub> |
| **📝 Text Summarization** | Streamlit app to summarize YouTube videos or Website URLs. <br><sub>*Tech:* <kbd>load_summarize_chain</kbd> <kbd>PromptTemplate</kbd></sub> |
| **🧮 MathsGPT** | Application to perform complex mathematical calculations accurately. <br><sub>*Tech:* <kbd>LLMMathChain</kbd> <kbd>StreamlitCallbackHandler</kbd></sub> |
| **🤗 Huggingface Integration**| Invoke open-source models directly using repo IDs and tokens. <br><sub>*Tech:* <kbd>HuggingFaceEndpoint</kbd></sub> |
| **📚 PDF-Query RAG** | Advanced document storage and querying using Cassandra. <br><sub>*Tech:* <kbd>AstraDB</kbd> <kbd>cassIO</kbd> <kbd>OllamaEmbeddings</kbd></sub> |
| **💻 CodeLlama Assistant** | Interactive coding assistant interface powered by REST APIs. <br><sub>*Tech:* <kbd>Gradio</kbd></sub> |
| **⚖️ Hybrid Search** | Combines keyword and vector search for better retrieval accuracy. <br><sub>*Tech:* <kbd>Pinecone</kbd> <kbd>HybridSearchRetriever</kbd></sub> |
| **🕸️ Graph Databases** | Knowledge graph creation and querying using Cypher language. <br><sub>*Tech:* <kbd>Neo4j</kbd> <kbd>GraphCypherQAChain</kbd></sub> |
| **⚙️ Fine Tuning LLMs** | Deep dive into training and optimizing model weights. <br><sub>*Tech:* <kbd>LoRA</kbd> <kbd>QLoRA</kbd> <kbd>Lamini API</kbd></sub> |
| **🔄 LangGraph** | State machine graphs to build robust, multi-agent AI systems. <br><sub>*Tech:* <kbd>StateGraph</kbd> <kbd>Nodes & Edges</kbd></sub> |

---

### ✨ 2) Google Gemini

This part consists of different projects created with the help of Gemini open source models. The idea is to use them using the `google.generativeai` library, and configure using the `GOOGLE_API_KEY`. These resources are from Udemy's [Building Gen AI App 12+ Hands-on Projects with Gemini Pro](https://www.udemy.com/course/building-gen-ai-app-end-to-end-projects-with-gemini-pro) course.

| <div align="center">🚀 Project<img width="175"/></div> | <div align="center">📝 Description<img width="600"/></div> |
| :--- | :--- |
| **🤖 LIM-LLM Application** | Streamlit apps using Gemini flash models for text and image chat. |
| **💬 Conversational Chatbot** | Chatbot application that interacts with an LLM with history using Gemini. |
| **🧾 Invoice Extractor** | App to extract data from invoices and answer specific queries. |
| **📚 Multiple PDF Chatbot** | Upload multiple PDFs and query seamlessly using <kbd>FAISS</kbd> and Gemini. |
| **🔍 Document QnA** | Simple <kbd>RAG</kbd> application for document-based QnA using the Gemini model. |
| **🗄️ Text-to-SQL-Querying** | Utilizes <kbd>sqlite3</kbd> to interact with an SQL database and display query outputs. |
| **📄 Resume ATS System** | Analyzes resumes against JDs and provide ATS-compliant feedback. |
| **🥗 Calorie Calculator** | Estimate calories from uploaded food images for diet tracking. |
| **▶️ Transcript Summarizer**| Generate concise summaries of YouTube video transcripts using Gemini. |

---
