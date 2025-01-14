from pydantic import BaseModel
from typing import List, Literal
from pathlib import Path
import yaml

class DirectorConfig(BaseModel):
    """Configuration for the AI Director"""
    prompt: str
    coder_model: str
    evaluator_model: Literal["gpt-4", "gpt-3.5-turbo"]
    max_iterations: int = 5
    execution_command: str
    context_editable: List[str]
    context_read_only: List[str]
    evaluator: Literal["default"] = "default"
    
    @classmethod
    def from_yaml(cls, config_path: Path) -> "DirectorConfig":
        """Load config from YAML file"""
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
            
        with open(config_path) as f:
            config_dict = yaml.safe_load(f)
            
        if config_dict["prompt"].endswith(".md"):
            prompt_path = Path(config_dict["prompt"])
            if not prompt_path.exists():
                raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
            with open(prompt_path) as f:
                config_dict["prompt"] = f.read()
                
        return cls(**config_dict)
