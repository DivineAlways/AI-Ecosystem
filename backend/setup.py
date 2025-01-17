from setuptools import setup, find_packages

setup(
    name="ai-ecosystem",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "pydantic>=2.4.2",
        "python-dotenv>=1.0.0",
        "httpx>=0.25.2",
        "python-jose>=3.3.0",
        "passlib>=1.7.4",
        "python-multipart>=0.0.6",
        "sqlalchemy>=2.0.23",
        "pytest>=7.4.3",
        "pytest-asyncio>=0.21.1",
        "openai>=1.10.0",
        "matplotlib>=3.8.2",
        "typer>=0.9.0",
        "rich>=13.7.0",
        "PyYAML>=6.0.1",
        "tenacity>=8.2.3"
    ],
)
