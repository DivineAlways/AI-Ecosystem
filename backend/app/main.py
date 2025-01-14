from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from .core.config import settings
from .core.output_format import format_output

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
    output_file: str | None = None,
    output_format: str = Query("json", enum=["json", "yaml", "text"])
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

        # Use word counter from agentic features
        from .core.word_counter import word_counter
        word_count_result = word_counter(text_content, min_count_threshold)
        
        # Generate charts if requested
        if chart_type:
            from .core.chart import create_bar_chart, create_pie_chart, create_line_chart
            chart_functions = {
                'bar': create_bar_chart,
                'pie': create_pie_chart,
                'line': create_line_chart
            }
            if chart_type in chart_functions:
                chart_functions[chart_type](word_count_result)
        
        # Use LLM for advanced analysis
        from .core.llm import analyze_transcript
        analysis_result = analyze_transcript(text_content, word_count_result.word_counts)
        
        analysis_result = {
            "word_counts": top_words,
            "quick_summary": f"Analysis of {len(words)} words and {len(sentences)} sentences.",
            "bullet_point_highlights": key_sentences,
            "sentiment_analysis": f"{sentiment} tone detected in the text",
            "keywords": keywords[:5]  # Top 5 keywords
        }
        
        # Format the output according to the requested format
        formatted_output = format_output(analysis_result, output_format)
        
        # If output file is specified, write the formatted output to file
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(formatted_output)
        
        # Return both raw and formatted data
        return {
            "raw": analysis_result,
            "formatted": formatted_output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    finally:
        if tmp_file_path and os.path.exists(tmp_file_path):
            try:
                os.remove(tmp_file_path)
            except:
                pass
