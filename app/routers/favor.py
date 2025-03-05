from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional
from app.api import favor

router = APIRouter(prefix="/favor", tags=["favor"])

# Models for request validation
class SyncRequest(BaseModel):
    appId: str
    syncKey: str

class GetContentRequest(BaseModel):
    appId: str
    favId: int

class DeleteRequest(BaseModel):
    appId: str
    favId: int

# Endpoint implementations
@router.post("/sync")
async def sync_favorites(request: SyncRequest):
    """Synchronize favorites"""
    return favor.sync(request.appId, request.syncKey)

@router.post("/getContent")
async def get_content(request: GetContentRequest):
    """Get favorite content"""
    return favor.get_content(request.appId, request.favId)

@router.post("/delete")
async def delete_favorite(request: DeleteRequest):
    """Delete favorite"""
    return favor.delete(request.appId, request.favId)