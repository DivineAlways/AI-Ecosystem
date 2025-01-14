#!/usr/bin/env python3
import typer
from app.director import Director

def main(config: str = "app/director/specs/basic.yaml"):
    """Run the AI Director with specified config"""
    director = Director(config)
    director.direct()

if __name__ == "__main__":
    typer.run(main)
