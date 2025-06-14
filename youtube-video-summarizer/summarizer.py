from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from youtube_transcript_api import YouTubeTranscriptApi
from groq_config import get_groq_llm

def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    else:
        return None

def fetch_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry['text'] for entry in transcript_list])

def summarize_transcript(transcript_text):
    llm = get_groq_llm()
    docs = [Document(page_content=transcript_text)]
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.run(docs)
    return summary
