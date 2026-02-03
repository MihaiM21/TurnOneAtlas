from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="Turn One Atlas",
    description="Telemetry SaaS API for racing data analysis",
    version="1.0.0"
)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
