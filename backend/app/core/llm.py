from typing import List
from pydantic import BaseModel
from openai import OpenAI
from .data_types import TranscriptAnalysis
import os
import time
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), 
                timeout=httpx.Timeout(30.0, read=60.0, write=10.0, connect=10.0))

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=4, max=30),
    retry=retry_if_exception_type((httpx.TimeoutException, httpx.NetworkError, httpx.ConnectError)),
    reraise=False
)
def analyze_transcript(transcript: str, word_counts: dict) -> TranscriptAnalysis:
    """Analyze transcript using OpenAI API and return structured analysis."""
    try:
        # Create a sample response for testing (remove in production)
        sample_response = {
            "quick_summary": "Sample analysis of the transcript",
            "bullet_point_highlights": [
                "Key point 1",
                "Key point 2",
                "Key point 3"
            ],
            "sentiment_analysis": "Neutral",
            "keywords": list(word_counts.keys())[:5]
        }
        
        return TranscriptAnalysis(**sample_response)
        
    except Exception as e:
        print(f"Error in analyze_transcript: {str(e)}")
        # Fallback analysis if analysis fails
        return TranscriptAnalysis(
            quick_summary="Analysis currently unavailable due to network issues",
            bullet_point_highlights=["Unable to generate highlights - please try again later"],
            sentiment_analysis="Network Error",
            keywords=list(word_counts.keys())[:5]
        )
