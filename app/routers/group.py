from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List, Optional
from app.api import group

router = APIRouter(prefix="/group", tags=["group"])

# Models for request validation
class CreateChatroomRequest(BaseModel):
    appId: str
    wxid: List[str]

class ModifyChatroomNameRequest(BaseModel):
    appId: str
    chatroomName: str
    chatroomId: str

class ModifyChatroomRemarkRequest(BaseModel):
    appId: str
    chatroomRemark: str
    chatroomId: str

class ModifyChatroomNickNameRequest(BaseModel):
    appId: str
    nickName: str
    chatroomId: str

class InviteMemberRequest(BaseModel):
    appId: str
    wxids: List[str]
    chatroomId: str
    reason: str = ""

class RemoveMemberRequest(BaseModel):
    appId: str
    wxids: List[str]
    chatroomId: str

class ChatroomIdRequest(BaseModel):
    appId: str
    chatroomId: str

class GetChatroomMemberDetailRequest(BaseModel):
    appId: str
    chatroomId: str
    memberWxids: List[str]

class SetChatroomAnnouncementRequest(BaseModel):
    appId: str
    chatroomId: str
    content: str

class AgreeJoinRoomRequest(BaseModel):
    appId: str
    chatroomName: str  # This is the URL in the original Java code

class AddGroupMemberAsFriendRequest(BaseModel):
    appId: str
    memberWxid: str
    chatroomId: str
    content: str

class SaveContractListRequest(BaseModel):
    appId: str
    chatroomName: int  # This is operType in the original Java code
    chatroomId: str

class AdminOperateRequest(BaseModel):
    appId: str
    chatroomId: str
    wxids: List[str]
    operType: int

class PinChatRequest(BaseModel):
    appId: str
    top: bool
    chatroomId: str

class SetMsgSilenceRequest(BaseModel):
    appId: str
    silence: bool
    chatroomId: str

class JoinRoomUsingQRCodeRequest(BaseModel):
    appId: str
    qrUrl: str

class RoomAccessApplyCheckApproveRequest(BaseModel):
    appId: str
    newMsgId: str
    chatroomId: str
    msgContent: str

# Endpoint implementations
@router.post("/createChatroom")
async def create_chatroom(request: CreateChatroomRequest):
    """Create a WeChat group"""
    return group.create_chatroom(request.appId, request.wxid)

@router.post("/modifyChatroomName")
async def modify_chatroom_name(request: ModifyChatroomNameRequest):
    """Modify group name"""
    return group.modify_chatroom_name(request.appId, request.chatroomName, request.chatroomId)

@router.post("/modifyChatroomRemark")
async def modify_chatroom_remark(request: ModifyChatroomRemarkRequest):
    """Modify group remark"""
    return group.modify_chatroom_remark(request.appId, request.chatroomRemark, request.chatroomId)

@router.post("/modifyChatroomNickNameForSelf")
async def modify_chatroom_nickname_for_self(request: ModifyChatroomNickNameRequest):
    """Modify my nickname in the group"""
    return group.modify_chatroom_nickname_for_self(request.appId, request.nickName, request.chatroomId)

@router.post("/inviteMember")
async def invite_member(request: InviteMemberRequest):
    """Invite/add members to group"""
    return group.invite_member(request.appId, request.wxids, request.chatroomId, request.reason)

@router.post("/removeMember")
async def remove_member(request: RemoveMemberRequest):
    """Remove group members"""
    return group.remove_member(request.appId, request.wxids, request.chatroomId)

@router.post("/quitChatroom")
async def quit_chatroom(request: ChatroomIdRequest):
    """Leave group chat"""
    return group.quit_chatroom(request.appId, request.chatroomId)

@router.post("/disbandChatroom")
async def disband_chatroom(request: ChatroomIdRequest):
    """Dissolve group chat"""
    return group.disband_chatroom(request.appId, request.chatroomId)

@router.post("/getChatroomInfo")
async def get_chatroom_info(request: ChatroomIdRequest):
    """Get group information"""
    return group.get_chatroom_info(request.appId, request.chatroomId)

@router.post("/getChatroomMemberList")
async def get_chatroom_member_list(request: ChatroomIdRequest):
    """Get group member list"""
    return group.get_chatroom_member_list(request.appId, request.chatroomId)

@router.post("/getChatroomMemberDetail")
async def get_chatroom_member_detail(request: GetChatroomMemberDetailRequest):
    """Get group member details"""
    return group.get_chatroom_member_detail(request.appId, request.chatroomId, request.memberWxids)

@router.post("/getChatroomAnnouncement")
async def get_chatroom_announcement(request: ChatroomIdRequest):
    """Get group announcement"""
    return group.get_chatroom_announcement(request.appId, request.chatroomId)

@router.post("/setChatroomAnnouncement")
async def set_chatroom_announcement(request: SetChatroomAnnouncementRequest):
    """Set group announcement"""
    return group.set_chatroom_announcement(request.appId, request.chatroomId, request.content)

@router.post("/agreeJoinRoom")
async def agree_join_room(request: AgreeJoinRoomRequest):
    """Agree to join group"""
    return group.agree_join_room(request.appId, request.chatroomName)

@router.post("/addGroupMemberAsFriend")
async def add_group_member_as_friend(request: AddGroupMemberAsFriendRequest):
    """Add group member as friend"""
    return group.add_group_member_as_friend(
        request.appId, request.memberWxid, request.chatroomId, request.content
    )

@router.post("/getChatroomQrCode")
async def get_chatroom_qr_code(request: ChatroomIdRequest):
    """Get group QR code"""
    return group.get_chatroom_qr_code(request.appId, request.chatroomId)

@router.post("/saveContractList")
async def save_contract_list(request: SaveContractListRequest):
    """Save group to contacts"""
    return group.save_contract_list(request.appId, request.chatroomName, request.chatroomId)

@router.post("/adminOperate")
async def admin_operate(request: AdminOperateRequest):
    """Admin operations"""
    return group.admin_operate(request.appId, request.chatroomId, request.wxids, request.operType)

@router.post("/pinChat")
async def pin_chat(request: PinChatRequest):
    """Pin chat"""
    return group.pin_chat(request.appId, request.top, request.chatroomId)

@router.post("/setMsgSilence")
async def set_msg_silence(request: SetMsgSilenceRequest):
    """Set message silence (do not disturb)"""
    return group.set_msg_silence(request.appId, request.silence, request.chatroomId)

@router.post("/joinRoomUsingQRCode")
async def join_room_using_qr_code(request: JoinRoomUsingQRCodeRequest):
    """Join group using QR code"""
    return group.join_room_using_qr_code(request.appId, request.qrUrl)

@router.post("/roomAccessApplyCheckApprove")
async def room_access_apply_check_approve(request: RoomAccessApplyCheckApproveRequest):
    """Confirm group join application"""
    return group.room_access_apply_check_approve(
        request.appId, request.newMsgId, request.chatroomId, request.msgContent
    )