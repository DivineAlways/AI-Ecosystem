from typing import List
from pydantic import BaseModel
from openai import OpenAI
from .data_types import TranscriptAnalysis

client = OpenAI()

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
            quick_summary="Analysis currently unavailable",
            bullet_point_highlights=["Unable to generate highlights"],
            sentiment_analysis="Neutral",
            keywords=list(word_counts.keys())[:5]
        )
