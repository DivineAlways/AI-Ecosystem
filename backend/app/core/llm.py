from typing import List
from pydantic import BaseModel
from openai import OpenAI
from .data_types import TranscriptAnalysis

client = OpenAI()

def analyze_transcript(transcript: str, word_counts: dict) -> TranscriptAnalysis:
    """Analyze transcript using OpenAI API and return structured analysis."""
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": """Analyze the transcript and provide:
                    1. A brief summary
                    2. Key bullet points
                    3. Sentiment analysis
                    4. Important keywords
                    Format as JSON matching the TranscriptAnalysis model."""
                },
                {"role": "user", "content": f"{transcript}\n\nWord Frequencies: {word_counts}"}
            ],
            response_format={"type": "json_object"}
        )
        
        response_content = completion.choices[0].message.content
        return TranscriptAnalysis.model_validate_json(response_content)
        
    except Exception as e:
        # Fallback analysis if API fails
        return TranscriptAnalysis(
            quick_summary="Analysis currently unavailable",
            bullet_point_highlights=["Unable to generate highlights"],
            sentiment_analysis="Neutral",
            keywords=list(word_counts.keys())[:5]
        )
