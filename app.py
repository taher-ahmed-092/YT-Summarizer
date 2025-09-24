import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import requests

# Load API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("🎬 YouTube Summarizer with Thumbnail")
st.subheader("Get AI-generated summaries of any YouTube video in 250 words or less")

# Input field
youtube_link = st.text_input("Enter YouTube Video Link")

# Extract video ID from any YouTube URL
def extract_video_id(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if hostname in ["youtu.be"]:
        return parsed.path[1:]
    elif hostname in ["www.youtube.com", "youtube.com", "m.youtube.com"]:
        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [None])[0]
        elif parsed.path.startswith("/embed/") or parsed.path.startswith("/v/"):
            return parsed.path.split("/")[2]
    return None

# Extract transcript if available
def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return " ".join([t["text"] for t in transcript_list])
    except:
        return None

# Get video title from YouTube API (public page scraping)
def get_video_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        res = requests.get(url)
        start = res.text.find('<title>') + len('<title>')
        end = res.text.find('</title>')
        title = res.text[start:end].replace(" - YouTube", "").strip()
        return title
    except:
        return "YouTube Video"

# Generate summary using Gemini
def generate_summary(prompt_text):
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    response = model.generate_content(prompt_text)  # pass as positional argument
    return response.text

# Main button
if st.button("Get Detailed Notes"):
    if youtube_link:
        video_id = extract_video_id(youtube_link)
        if video_id:
            # Display thumbnail
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
            st.image(thumbnail_url, caption="Video Thumbnail", use_column_width=True)
            
            # Get transcript
            transcript = get_transcript(video_id)
            title = get_video_title(video_id)
            
            if transcript:
                prompt = f"Summarize the YouTube video titled '{title}' in 250 words or less, highlighting key points:\n\n{transcript}"
            else:
                prompt = f"Summarize the YouTube video titled '{title}' in 250 words or less based on the title and key points."
            
            # Generate summary
            summary = generate_summary(prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
        else:
            st.error("Invalid YouTube link.")
    else:
        st.warning("Please enter a YouTube link.")

# Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
        <p>⚡ Built with Streamlit & Python | © 2025 Taher</p>
    </div>
    """,
    unsafe_allow_html=True
)