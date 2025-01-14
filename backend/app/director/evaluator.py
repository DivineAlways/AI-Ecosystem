from pydantic import BaseModel
from typing import Optional
from pathlib import Path
from openai import OpenAI
import json

class EvaluationResult(BaseModel):
    """Result of evaluating code execution"""
    success: bool
    feedback: Optional[str] = None

class Evaluator:
    def __init__(self, model: str):
        self.model = model
        self.client = OpenAI()
        
    def evaluate(self, 
                execution_output: str,
                prompt: str,
                editable_files: dict[str, str],
                read_only_files: dict[str, str],
                execution_command: str) -> EvaluationResult:
        """Evaluate execution output against requirements"""
        
        evaluation_prompt = self._build_evaluation_prompt(
            execution_output=execution_output,
            prompt=prompt,
            editable_files=editable_files,
            read_only_files=read_only_files,
            execution_command=execution_command
        )

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": evaluation_prompt}],
                response_format={"type": "json_object"}
            )
            
            result = json.loads(completion.choices[0].message.content)
            return EvaluationResult(**result)
            
        except Exception as e:
            return EvaluationResult(
                success=False,
                feedback=f"Evaluation failed: {str(e)}"
            )
            
    def _build_evaluation_prompt(self,
                               execution_output: str,
                               prompt: str,
                               editable_files: dict[str, str],
                               read_only_files: dict[str, str],
                               execution_command: str) -> str:
        """Build the evaluation prompt"""
        return f"""Evaluate this execution output and determine if it was successful.

## Checklist:
- Is the execution output reporting success or failure?
- Did we miss any tasks? Review the User's Desired Result.
- Did we satisfy all requirements?
- Ignore warnings

## User's Desired Result:
{prompt}

## Editable Files:
{editable_files}

## Read-Only Files:
{read_only_files}

## Execution Command:
{execution_command}
                                        
## Execution Output:
{execution_output}

Return JSON with:
{{
    "success": boolean,
    "feedback": string or null
}}"""
