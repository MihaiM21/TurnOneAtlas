# Turn One Atlas

Atlas - Powered by Turn One

A telemetry SaaS backend MVP for processing and analyzing racing telemetry data.

## Tech Stack

- **Python 3.12+**
- **FastAPI** - Modern, fast web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Pandas** - CSV data processing

## Project Structure

```
TurnOneAtlas/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py      # API route handlers
│   ├── core/
│   │   ├── __init__.py
│   │   └── telemetry.py      # Telemetry processing logic
│   ├── models/
│   │   ├── __init__.py
│   │   └── responses.py      # Pydantic response models
│   └── __init__.py
├── main.py                   # FastAPI application entry point
└── requirements.txt          # Python dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MihaiM21/TurnOneAtlas.git
cd TurnOneAtlas
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
```
GET /health
```

Returns the status of the API.

**Response:**
```json
{
  "status": "healthy",
  "message": "Turn One Atlas API is running"
}
```

### Upload Telemetry CSV
```
POST /upload
```

Upload a CSV file containing telemetry data. Returns the number of samples and available channels.

**Request:**
- Content-Type: `multipart/form-data`
- Body: CSV file

**Response:**
```json
{
  "status": "success",
  "samples": 10,
  "channels": ["time", "speed", "throttle", "brake", "rpm"]
}
```

## API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Example Usage

Using curl:
```bash
# Health check
curl http://localhost:8000/health

# Upload telemetry CSV
curl -X POST -F "file=@telemetry.csv" http://localhost:8000/upload
```

## CSV Format

The API accepts CSV files with any structure. Example:
```csv
time,speed,throttle,brake,rpm
0.0,0,0,0,1000
0.1,10,0.2,0,1500
0.2,20,0.4,0,2000
```

## Development

This is an MVP with minimal features. Future enhancements may include:
- Data visualization
- Advanced analytics
- Real-time telemetry streaming
- Multi-user support
- Data persistence
