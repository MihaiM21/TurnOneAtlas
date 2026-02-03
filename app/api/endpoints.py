from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.responses import HealthResponse, TelemetryUploadResponse
from app.core.telemetry import process_telemetry_csv

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return HealthResponse(
        status="healthy",
        message="Turn One Atlas API is running"
    )


@router.post("/upload", response_model=TelemetryUploadResponse)
async def upload_telemetry(file: UploadFile = File(...)):
    """
    Upload and process CSV telemetry file.
    
    Returns basic information about the telemetry data:
    - Number of samples
    - Available channels (column names)
    """
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported"
        )
    
    try:
        content = await file.read()
        result = process_telemetry_csv(content)
        
        return TelemetryUploadResponse(
            status="success",
            samples=result["samples"],
            channels=result["channels"]
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing CSV file: {str(e)}"
        )
