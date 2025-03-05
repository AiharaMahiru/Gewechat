from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.utils.http_client import HttpClient

# Import all routers
from app.routers import message, login, personal, group, label, favor, download, contact

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up configuration
HttpClient.base_url = settings.API_BASE_URL
HttpClient.token = settings.API_TOKEN

# Include all routers
app.include_router(message.router, prefix="/api/message", tags=["Message"])
app.include_router(login.router, prefix="/api/login", tags=["Login"])
app.include_router(personal.router, prefix="/api/personal", tags=["Personal"])
app.include_router(group.router, prefix="/api/group", tags=["Group"])
app.include_router(label.router, prefix="/api/label", tags=["Label"])
app.include_router(favor.router, prefix="/api/favor", tags=["Favor"])
app.include_router(download.router, prefix="/api/download", tags=["Download"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])

@app.get("/")
async def root():
    """
    Root endpoint that returns basic API information
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)