import os
import tempfile
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from agentic_features.paicc_7.src.let_the_code_write_itself.main import analyze_transcript as paicc_analyze_transcript
from agentic_features.paicc_7.src.let_the_code_write_itself.data_types import TranscriptAnalysis
from pydantic import BaseModel
from fastapi import UploadFile, File

class AnalysisRequest(BaseModel):
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
async def analyze_transcript(
    min_count_threshold: int = 10,
    chart_type: str | None = None,
    output_file: str | None = None,
    transcript: UploadFile = File(...)
):
    if not transcript or not transcript.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    if not transcript.filename.endswith(('.txt', '.text')):
        raise HTTPException(status_code=400, detail="File must be a text file (.txt or .text)")

    tmp_file_path = None
    try:
        # Read file content first to validate
        content = await transcript.read()
        if not content:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        try:
            text_content = content.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="File must be a valid UTF-8 text file")

        # Create temporary file and write content
        tmp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt")
        tmp_file_path = tmp_file.name
        
        with open(tmp_file_path, "w", encoding="utf-8") as f:
            f.write(text_content)

        # Call the paicc analyze_transcript function with the temporary file path
        analysis_result = paicc_analyze_transcript(
            path_to_script_text_file=tmp_file_path,
            min_count_threshold=min_count_threshold,
            chart_type=chart_type,
            output_file=output_file
        )
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    finally:
        # Always clean up the temporary file
        if tmp_file_path and os.path.exists(tmp_file_path):
            try:
                os.remove(tmp_file_path)
            except:
                pass  # Ignore cleanup errors
