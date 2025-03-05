from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional
from app.api import personal

router = APIRouter(prefix="/personal", tags=["personal"])

# Models for request validation
class AppIdRequest(BaseModel):
    appId: str

class PrivacySettingsRequest(BaseModel):
    appId: str
    option: int
    open: bool

class UpdateProfileRequest(BaseModel):
    appId: str
    city: str
    country: str
    nickName: str
    province: str
    sex: str
    signature: str

class UpdateHeadImgRequest(BaseModel):
    appId: str
    headImgUrl: str

# Endpoint implementations
@router.post("/getProfile")
async def get_profile(request: AppIdRequest):
    """Get personal profile"""
    return personal.get_profile(request.appId)

@router.post("/getQrCode")
async def get_qr_code(request: AppIdRequest):
    """Get personal QR code"""
    return personal.get_qr_code(request.appId)

@router.post("/getSafetyInfo")
async def get_safety_info(request: AppIdRequest):
    """Get device records"""
    return personal.get_safety_info(request.appId)

@router.post("/privacySettings")
async def privacy_settings(request: PrivacySettingsRequest):
    """Adjust privacy settings"""
    return personal.privacy_settings(request.appId, request.option, request.open)

@router.post("/updateProfile")
async def update_profile(request: UpdateProfileRequest):
    """Update personal profile information"""
    return personal.update_profile(
        request.appId,
        request.city,
        request.country,
        request.nickName,
        request.province,
        request.sex,
        request.signature
    )

@router.post("/updateHeadImg")
async def update_head_img(request: UpdateHeadImgRequest):
    """Update profile picture"""
    return personal.update_head_img(request.appId, request.headImgUrl)