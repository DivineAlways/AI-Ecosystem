from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}

@app.post("/analyze-transcript")
async def analyze_transcript(
    transcript: UploadFile = File(...),
    chart_type: str | None = None,
    min_count_threshold: int = 10,
    output_file: str | None = None
) -> dict:
    if not transcript or not transcript.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    if not transcript.filename.endswith(('.txt', '.text')):
        raise HTTPException(status_code=400, detail="File must be a text file (.txt or .text)")

    tmp_file_path = None
    try:
        content = await transcript.read()
        if not content:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        try:
            text_content = content.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="File must be a valid UTF-8 text file")

        tmp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt")
        tmp_file_path = tmp_file.name
        
        with open(tmp_file_path, "w", encoding="utf-8") as f:
            f.write(text_content)

        # Perform actual analysis on the text content
        words = text_content.lower().split()
        
        # Calculate word frequencies
        word_counts = {}
        for word in words:
            if len(word) > 2:  # Skip very short words
                word_counts[word] = word_counts.get(word, 0) + 1
        
        # Sort by frequency and get top words
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        top_words = dict(sorted_words[:10])
        
        # Extract sentences for bullet points
        sentences = [s.strip() for s in text_content.split('.') if s.strip()]
        key_sentences = sentences[:3]  # Take first 3 sentences as highlights
        
        # Basic sentiment analysis
        positive_words = {'improve', 'transforming', 'future', 'help', 'automated'}
        negative_words = {'complex', 'difficult', 'problem', 'issue'}
        
        sentiment_score = sum(1 for word in words if word in positive_words)
        sentiment_score -= sum(1 for word in words if word in negative_words)
        
        sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
        
        # Extract keywords (words that appear more than once)
        keywords = [word for word, count in word_counts.items() if count > 1]
        
        return {
            "word_counts": top_words,
            "quick_summary": f"Analysis of {len(words)} words and {len(sentences)} sentences.",
            "bullet_point_highlights": key_sentences,
            "sentiment_analysis": f"{sentiment} tone detected in the text",
            "keywords": keywords[:5]  # Top 5 keywords
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    finally:
        if tmp_file_path and os.path.exists(tmp_file_path):
            try:
                os.remove(tmp_file_path)
            except:
                pass
