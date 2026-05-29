import os
from crewai import Crew, Process, LLM
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

## Define an open-source model explicitly via NVIDIA endpoints
open_source_llm = LLM(
    model="meta/llama-3.1-70b-instruct",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY")
)

## Explicitly ensure your imported agents are utilizing this LLM configuration
blog_researcher.llm = open_source_llm
blog_writer.llm = open_source_llm

## Form the tech-focused crew
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = False
)

if __name__ == "__main__":
    ## Start the task execution process
    result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
    print("\n--- CREW EXECUTION RESULT ---")
    print(result)