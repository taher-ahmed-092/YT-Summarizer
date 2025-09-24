# 🎬 YouTube Summarizer with AI

A Streamlit-based AI application that generates detailed summaries of YouTube videos in **250 words or less** using **Google Gemini**. This project demonstrates practical use of generative AI to analyze video transcripts and provide concise insights.

---

## **Features**

- **AI-Powered Summarization**
  - Uses Google Gemini to summarize YouTube videos based on transcripts.
  - Generates clear, concise notes highlighting key points.

- **Supports Multiple YouTube URLs**
  - Handles `youtu.be` short links, standard YouTube links, and embedded URLs.

- **Transcript Extraction**
  - Retrieves video transcripts automatically (if available in English).
  - Falls back to title-based summarization if transcript is unavailable.

- **Interactive Streamlit Interface**
  - Upload video link and instantly get AI-generated notes.
  - Displays video thumbnail for context.

- **Error Handling**
  - Detects invalid YouTube links.
  - Warns when no link is entered or transcript is missing.

---

## **Usage**

1. Open the Streamlit app in your browser.  
2. Enter the YouTube video URL in the input box.  
3. Click **Get Detailed Notes**.  
4. View AI-generated summary along with video thumbnail.

---

## **Notes**

- `.env` file contains the **Google Generative AI API key** and is excluded from GitHub using `.gitignore`.  
- Ensure `requirements.txt` is installed to run the app.  
- Uses safety measures in the AI model for ethical and unbiased summarization.  

---

## **Tech Stack**

- Python 3.x  
- [Streamlit](https://streamlit.io/) for UI  
- [Google Generative AI](https://developers.generativeai.google/) (Gemini 1.5) for summarization  
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variables  
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) for transcript extraction  
- [requests](https://pypi.org/project/requests/) for video metadata extraction  

---

## **License**

This project is intended for educational and professional demonstration purposes. Modify as needed for production use.
