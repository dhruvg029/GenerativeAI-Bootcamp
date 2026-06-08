import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

## Loading the environment variables
load_dotenv()

## Loading the google api key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Function to extract the transcript from the youtube url
def extract_transcript_details(youtube_link):
    try:
        ## Extracting the video ID from the URL
        video_id = youtube_link.split("=")[1]
        
        ## Initializing the API and fetch
        yt_api = YouTubeTranscriptApi()
        transcript_list = yt_api.fetch(video_id)
        
        ## Initializing the empty string
        transcript = ""
        
        ## Iterating through the objects
        for snippet in transcript_list:
            transcript += " " + snippet.text
            
        return transcript
        
    except Exception as e:
        raise e

## Function to generate gemini content
def generate_gemini_content(transcript_text, prompt):
    """
    Function to generate gemini content
    """
    model = genai.GenerativeModel('gemini-3.5-flash')
    response = model.generate_content(prompt + transcript_text)
    return response.text

prompt = """
You are a YouTube video summarizer. You will be taking the transcript text and summarizing the entire video 
and provide the important summary in bullet points in a clear and concise manner, within 250 words.
Please provide the summary of the text given here, in a well-structured and organized manner.
"""

st.title("YouTube Video Summarizer using Gemini")
st.text("Summarize the youtube video in a few words")

youtube_link = st.text_input("Enter the youtube video url here...")

if youtube_link:

    ## Extracting the video id
    video_id = youtube_link.split("=")[1] 
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", width = 600)

if st.button("Get the summary"):
    
    ## Extracting the transcript details
    transcript_text = extract_transcript_details(youtube_link)

    ## Checking if the transcript is extracted
    if transcript_text:
        
        st.markdown("## Summary of the video: ")

        ## Generating the summary
        summary = generate_gemini_content(transcript_text, prompt)

        st.markdown(summary)
    