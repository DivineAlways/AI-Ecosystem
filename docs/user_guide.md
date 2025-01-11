# AI-Ecosystem User Guide

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
│   │   └── core/
│   │       └── config.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_main.py
│   └── requirements.txt
├── frontend/
├── docker/
└── pytest.ini
```

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
