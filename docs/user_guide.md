# AI-Ecosystem User Guide

## Overview

AI-Ecosystem is an advanced AI-powered platform that combines transcript analysis capabilities with an AI Director system for automated code improvements.

## System Requirements

- Python 3.12+
- Node.js 16+
- Docker and Docker Compose (optional)
- PostgreSQL (if not using Docker)

## Installation

### Backend Setup

1. Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file with required variables:
     - DATABASE_URL
     - SECRET_KEY

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

## Running the System

### Development Mode

1. Start the backend server:
```bash
cd backend
uvicorn app.main:app --reload
```
The API will be available at http://localhost:8000

2. Start the frontend development server:
```bash
cd frontend
npm run serve
```
The frontend will be available at http://localhost:8080

### Running Tests

To run the backend tests:
```bash
cd backend
PYTHONPATH=$PWD pytest tests/ -v
```

### Using Docker (Alternative)

To run the entire system using Docker:

```bash
docker-compose up --build
```

This will start:
- Backend API at http://localhost:8000
- Frontend at http://localhost:8080
- PostgreSQL database at localhost:5432

## API Documentation

Once the backend is running, you can access:
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   └── config.py
│   │   └── director/
│   │       ├── __init__.py
│   │       ├── director.py
│   │       ├── evaluator.py
│   │       └── specs/
│   │           └── basic.yaml
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_main.py
│   └── requirements.txt
├── frontend/
├── docker/
└── pytest.ini
```

## AI Director

The AI Director is a self-improving system that can automatically enhance code quality. It works through an iterative process of:
1. Analyzing existing code
2. Generating improvements
3. Testing changes
4. Evaluating results

### Using the AI Director

1. Install the package in development mode:
```bash
cd backend
pip install -e .
```

2. Run the director with default configuration:
```bash
python run_director.py
```

3. Or specify a custom config file:
```bash
python run_director.py --config path/to/config.yaml
```

### Configuration

The AI Director is configured through YAML files in `backend/app/director/specs/`. Key settings include:

- `prompt`: The improvement goal
- `coder_model`: AI model for code generation (gpt-4 or gpt-3.5-turbo)
- `evaluator_model`: AI model for evaluation
- `max_iterations`: Maximum improvement attempts
- `execution_command`: Command to validate changes
- `context_editable`: Files that can be modified
- `context_read_only`: Reference-only files

## Security Notes

- The default configuration is for development only
- For production:
  - Update SECRET_KEY in .env
  - Configure proper CORS settings
  - Enable HTTPS
  - Set up proper database credentials

## Troubleshooting

Common issues:

1. Module not found errors:
   - Ensure PYTHONPATH is set correctly
   - Check that your virtual environment is activated
   - Verify all dependencies are installed

2. Database connection errors:
   - Check DATABASE_URL in .env
   - Ensure PostgreSQL is running
   - Verify database exists and credentials are correct

3. Test failures:
   - Ensure you're running tests from the correct directory
   - Check PYTHONPATH is set correctly
   - Verify test dependencies are installed

## Version History

- v0.1.0 - Initial setup with FastAPI backend and Vue.js frontend
- v0.1.1 - Added testing infrastructure and documentation
