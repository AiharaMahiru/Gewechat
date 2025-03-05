from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional
from app.api import login

router = APIRouter(prefix="/login", tags=["login"])

# Models for request validation
class TokenRequest(BaseModel):
    pass  # Empty request body for getToken

class CallbackRequest(BaseModel):
    token: str
    callbackUrl: str

class QrCodeRequest(BaseModel):
    appId: str = ""

class CheckLoginRequest(BaseModel):
    appId: str
    uuid: str
    captchCode: str = ""

class AppIdRequest(BaseModel):
    appId: str

# Endpoint implementations
@router.post("/getTokenId", tags=["tools"])
async def get_token():
    """Get token ID"""
    return login.get_token()

@router.post("/setCallback", tags=["tools"])
async def set_callback(request: CallbackRequest):
    """Set callback URL for WeChat messages"""
    return login.set_callback(request.token, request.callbackUrl)

@router.post("/getLoginQrCode")
async def get_login_qrcode(request: QrCodeRequest):
    """Get login QR code"""
    return login.get_qr(request.appId)

@router.post("/checkLogin")
async def check_login(request: CheckLoginRequest):
    """Check login status"""
    return login.check_qr(request.appId, request.uuid, request.captchCode)

@router.post("/logout")
async def logout(request: AppIdRequest):
    """Logout from WeChat"""
    return login.logout(request.appId)

@router.post("/dialogLogin")
async def dialog_login(request: AppIdRequest):
    """Dialog login"""
    return login.dialog_login(request.appId)

@router.post("/checkOnline")
async def check_online(request: AppIdRequest):
    """Check if user is online"""
    return login.check_online(request.appId)