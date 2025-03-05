from fastapi import APIRouter, Body, Query
from pydantic import BaseModel
from typing import List, Optional
from app.api import message

router = APIRouter(prefix="/message", tags=["message"])

# Models for request validation
class TextMessageRequest(BaseModel):
    appId: str
    toWxid: str
    content: str
    ats: str = ""

class FileMessageRequest(BaseModel):
    appId: str
    toWxid: str
    fileUrl: str
    fileName: str

class ImageMessageRequest(BaseModel):
    appId: str
    toWxid: str
    imgUrl: str

class VoiceMessageRequest(BaseModel):
    appId: str
    toWxid: str
    voiceUrl: str
    voiceDuration: int

class VideoMessageRequest(BaseModel):
    appId: str
    toWxid: str
    videoUrl: str
    thumbUrl: str
    videoDuration: int

class LinkMessageRequest(BaseModel):
    appId: str
    toWxid: str
    title: str
    desc: str
    linkUrl: str
    thumbUrl: str

class NameCardMessageRequest(BaseModel):
    appId: str
    toWxid: str
    nickName: str
    nameCardWxid: str

class EmojiMessageRequest(BaseModel):
    appId: str
    toWxid: str
    emojiMd5: str
    emojiSize: str

class AppMsgRequest(BaseModel):
    appId: str
    toWxid: str
    appmsg: str

class MiniAppMessageRequest(BaseModel):
    appId: str
    toWxid: str
    miniAppId: str
    displayName: str
    pagePath: str
    coverImgUrl: str
    title: str
    userName: str

class ForwardRequest(BaseModel):
    appId: str
    toWxid: str
    xml: str
    coverImgUrl: Optional[str] = None

class RevokeMsgRequest(BaseModel):
    appId: str
    toWxid: str
    msgId: str
    newMsgId: str
    createTime: str

# Endpoint implementations
@router.post("/postText")
async def post_text(request: TextMessageRequest):
    """Send text message"""
    return message.post_text(
        request.appId, request.toWxid, request.content, request.ats
    )

@router.post("/postFile")
async def post_file(request: FileMessageRequest):
    """Send file message"""
    return message.post_file(
        request.appId, request.toWxid, request.fileUrl, request.fileName
    )

@router.post("/postImage")
async def post_image(request: ImageMessageRequest):
    """Send image message"""
    return message.post_image(request.appId, request.toWxid, request.imgUrl)

@router.post("/postVoice")
async def post_voice(request: VoiceMessageRequest):
    """Send voice message"""
    return message.post_voice(
        request.appId, request.toWxid, request.voiceUrl, request.voiceDuration
    )

@router.post("/postVideo")
async def post_video(request: VideoMessageRequest):
    """Send video message"""
    return message.post_video(
        request.appId, request.toWxid, request.videoUrl, 
        request.thumbUrl, request.videoDuration
    )

@router.post("/postLink")
async def post_link(request: LinkMessageRequest):
    """Send link message"""
    return message.post_link(
        request.appId, request.toWxid, request.title, 
        request.desc, request.linkUrl, request.thumbUrl
    )

@router.post("/postNameCard")
async def post_name_card(request: NameCardMessageRequest):
    """Send name card message"""
    return message.post_name_card(
        request.appId, request.toWxid, request.nickName, request.nameCardWxid
    )

@router.post("/postEmoji")
async def post_emoji(request: EmojiMessageRequest):
    """Send emoji message"""
    return message.post_emoji(
        request.appId, request.toWxid, request.emojiMd5, request.emojiSize
    )

@router.post("/postAppMsg")
async def post_app_msg(request: AppMsgRequest):
    """Send app message"""
    return message.post_app_msg(request.appId, request.toWxid, request.appmsg)

@router.post("/postMiniApp")
async def post_mini_app(request: MiniAppMessageRequest):
    """Send mini app message"""
    return message.post_mini_app(
        request.appId, request.toWxid, request.miniAppId,
        request.displayName, request.pagePath, request.coverImgUrl,
        request.title, request.userName
    )

@router.post("/forwardFile")
async def forward_file(request: ForwardRequest):
    """Forward file"""
    return message.forward_file(request.appId, request.toWxid, request.xml)

@router.post("/forwardImage")
async def forward_image(request: ForwardRequest):
    """Forward image"""
    return message.forward_image(request.appId, request.toWxid, request.xml)

@router.post("/forwardVideo")
async def forward_video(request: ForwardRequest):
    """Forward video"""
    return message.forward_video(request.appId, request.toWxid, request.xml)

@router.post("/forwardUrl")
async def forward_url(request: ForwardRequest):
    """Forward URL"""
    return message.forward_url(request.appId, request.toWxid, request.xml)

@router.post("/forwardMiniApp")
async def forward_mini_app(request: ForwardRequest):
    """Forward mini app"""
    return message.forward_mini_app(
        request.appId, request.toWxid, request.xml, request.coverImgUrl
    )

@router.post("/revokeMsg")
async def revoke_msg(request: RevokeMsgRequest):
    """Revoke message"""
    return message.revoke_msg(
        request.appId, request.toWxid, request.msgId, 
        request.newMsgId, request.createTime
    )