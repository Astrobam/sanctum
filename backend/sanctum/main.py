# backend/sanctum/main.py

from fastapi import FastAPI
from sanctum.routers import auth

# Create the main FastAPI application instance
app = FastAPI(
    title="Sanctum API",
    description="The backend service for the Sanctum AI companion application.",
    version="0.1.0",
)

# Include the authentication router
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])

@app.get("/", tags=["Root"])
def read_root():
    """
    A simple welcome endpoint for the API.
    """
    return {"message": "Welcome to the Sanctum API"}
