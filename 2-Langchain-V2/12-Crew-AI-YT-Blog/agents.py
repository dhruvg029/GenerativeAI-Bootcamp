from crewai import Agent, Task, Crew, LLM
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

## Get the NVIDIA LLM
nvidia_llm = LLM(
    model = "meta/llama-3.1-70b-instruct",
    base_url = "https://integrate.api.nvidia.com/v1/",
    api_key = os.environ.get("NVIDIA_API_KEY")
)

## Create a senior blog content researcher
blog_researcher = Agent(
    role = 'Blog researcher from youtube videos',
    goal = 'get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose = True,
    memory = True,
    backstory = (
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    llm = nvidia_llm,
    tools = [yt_tool],
    allow_delegation = True
)

## creating a senior blog writer agent with YT tool
blog_writer = Agent(
    role = 'Blog writer',
    goal = 'Narrate compelling tech stories about the video {topic} from YT video',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    llm = nvidia_llm,
    tools = [yt_tool],
    allow_delegation = False
)