from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional
from app.api import download

router = APIRouter(prefix="/message", tags=["download"])

# Models for request validation
class DownloadImageRequest(BaseModel):
    appId: str
    xml: str
    type: int

class DownloadVoiceRequest(BaseModel):
    appId: str
    xml: str
    msgId: int

class DownloadVideoRequest(BaseModel):
    appId: str
    xml: str

class DownloadEmojiRequest(BaseModel):
    appId: str
    emojiMd5: str

class DownloadCdnRequest(BaseModel):
    appId: str
    aesKey: str
    fileId: str
    type: str
    totalSize: str
    suffix: str

# Endpoint implementations
@router.post("/downloadImage")
async def download_image(request: DownloadImageRequest):
    """Download image"""
    return download.download_image(request.appId, request.xml, request.type)

@router.post("/downloadVoice")
async def download_voice(request: DownloadVoiceRequest):
    """Download voice message"""
    return download.download_voice(request.appId, request.xml, request.msgId)

@router.post("/downloadVideo")
async def download_video(request: DownloadVideoRequest):
    """Download video"""
    return download.download_video(request.appId, request.xml)

@router.post("/downloadEmojiMd5")
async def download_emoji_md5(request: DownloadEmojiRequest):
    """Download emoji by MD5"""
    return download.download_emoji_md5(request.appId, request.emojiMd5)

@router.post("/downloadCdn")
async def download_cdn(request: DownloadCdnRequest):
    """Download from CDN"""
    return download.download_image(
        request.appId, request.aesKey, request.fileId, 
        request.type, request.totalSize, request.suffix
    )