from pathlib import Path
import subprocess
from typing import Optional
from .config import DirectorConfig
from .evaluator import Evaluator, EvaluationResult
from aider.coders import Coder
from aider.models import Model
from aider.io import InputOutput
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Director:
    """Self-Directed AI Coding Assistant"""
    
    def __init__(self, config_path: str):
        self.config = DirectorConfig.from_yaml(Path(config_path))
        self.evaluator = Evaluator(self.config.evaluator_model)
        
    def direct(self):
        """Main direction loop"""
        success = False
        execution_output = ""
        evaluation = EvaluationResult(success=False)
        
        for iteration in range(self.config.max_iterations):
            logger.info(f"\nIteration {iteration+1}/{self.config.max_iterations}")
            
            # Generate new prompt
            new_prompt = self._create_prompt(iteration, execution_output, evaluation)
            
            # Generate code
            self._generate_code(new_prompt)
            
            # Execute and evaluate
            execution_output = self._execute()
            evaluation = self._evaluate(execution_output)
            
            if evaluation.success:
                success = True
                logger.info(f"Success achieved after {iteration+1} iterations!")
                break
                
        if not success:
            logger.warning("Failed to achieve success within max iterations")
            
    def _create_prompt(self, 
                      iteration: int,
                      execution_output: str,
                      evaluation: EvaluationResult) -> str:
        """Create the next iteration prompt"""
        if iteration == 0:
            return self.config.prompt
            
        return f"""
# Generate the next iteration based on previous feedback

## Iteration {iteration+1}/{self.config.max_iterations}
> {self.config.max_iterations - iteration} attempts remaining

## Original Instructions:
{self.config.prompt}

## Previous Output:
{execution_output}

## Feedback:
{evaluation.feedback}"""

    def _generate_code(self, prompt: str):
        """Generate code using Aider"""
        model = Model("gpt-4" if self.config.coder_model == "gpt-4o" else "gpt-3.5-turbo")
        coder = Coder.create(
            main_model=model,
            io=InputOutput(yes=True),
            fnames=[str(Path(os.getcwd()) / f) for f in self.config.context_editable],
            read_only_fnames=[str(Path(os.getcwd()) / f) for f in self.config.context_read_only],
            auto_commits=False
        )
        coder.run(prompt)
        
    def _execute(self) -> str:
        """Execute the code"""
        try:
            result = subprocess.run(
                self.config.execution_command.split(),
                capture_output=True,
                text=True
            )
            return result.stdout + result.stderr
        except Exception as e:
            return f"Execution failed: {str(e)}"
            
    def _evaluate(self, execution_output: str) -> EvaluationResult:
        """Evaluate the execution results"""
        editable_files = {
            Path(fname).name: Path(fname).read_text()
            for fname in self.config.context_editable
        }
        
        read_only_files = {
            Path(fname).name: Path(fname).read_text()
            for fname in self.config.context_read_only
        }
        
        return self.evaluator.evaluate(
            execution_output=execution_output,
            prompt=self.config.prompt,
            editable_files=editable_files,
            read_only_files=read_only_files,
            execution_command=self.config.execution_command
        )
