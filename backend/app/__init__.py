from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from ..core.config import settings
from agentic_features.paicc_7.src.let_the_code_write_itself.main import analyze_transcript as paicc_analyze_transcript
from agentic_features.paicc_7.src.let_the_code_write_itself.data_types import TranscriptAnalysis
from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    transcript: str
    min_count_threshold: int = 10
    chart_type: str | None = None
    output_file: str | None = None

app = FastAPI(title="AI-Ecosystem")

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
    return {"message": "Welcome to AI-Ecosystem API"}

@app.post("/analyze-transcript", response_model=TranscriptAnalysis)
async def analyze_transcript(request: AnalysisRequest):
    try:
        # Call the paicc analyze_transcript function
        analysis_result = paicc_analyze_transcript(
            path_to_script_text_file=request.transcript,
            min_count_threshold=request.min_count_threshold,
            chart_type=request.chart_type,
            output_file=request.output_file
        )
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
