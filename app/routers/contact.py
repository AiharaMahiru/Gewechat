from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List, Optional
from app.api import contact

router = APIRouter(prefix="/contacts", tags=["contacts"])

# Models for request validation
class AppIdRequest(BaseModel):
    appId: str

class GetBriefInfoRequest(BaseModel):
    appId: str
    wxids: List[str]

class GetDetailInfoRequest(BaseModel):
    appId: str
    wxids: List[str]

class SearchRequest(BaseModel):
    appId: str
    contactsInfo: str

class AddContactsRequest(BaseModel):
    appId: str
    scene: int
    option: int
    v3: str
    v4: str
    content: str

class DeleteFriendRequest(BaseModel):
    appId: str
    wxid: str

class SetFriendPermissionsRequest(BaseModel):
    appId: str
    wxid: str
    onlyChat: bool

class SetFriendRemarkRequest(BaseModel):
    appId: str
    wxid: str
    onlyChat: str  # This is 'remark' in the original Java code

class GetPhoneAddressListRequest(BaseModel):
    appId: str
    wxid: List[str]  # This is 'phones' in the original Java code

class UploadPhoneAddressListRequest(BaseModel):
    appId: str
    wxid: List[str]  # This is 'phones' in the original Java code
    opType: int

# Endpoint implementations
@router.post("/fetchContactsList")
async def fetch_contacts_list(request: AppIdRequest):
    """Get contact list"""
    return contact.fetch_contacts_list(request.appId)

@router.post("/getBriefInfo")
async def get_brief_info(request: GetBriefInfoRequest):
    """Get brief info about groups/friends"""
    return contact.get_brief_info(request.appId, request.wxids)

@router.post("/getDetailInfo")
async def get_detail_info(request: GetDetailInfoRequest):
    """Get detailed info about groups/friends"""
    return contact.get_detail_info(request.appId, request.wxids)

@router.post("/search")
async def search_contacts(request: SearchRequest):
    """Search for friends"""
    return contact.search(request.appId, request.contactsInfo)

@router.post("/addContacts")
async def add_contacts(request: AddContactsRequest):
    """Add contacts/accept friend requests"""
    return contact.add_contacts(
        request.appId, request.scene, request.option, 
        request.v3, request.v4, request.content
    )

@router.post("/deleteFriend")
async def delete_friend(request: DeleteFriendRequest):
    """Delete friend"""
    return contact.delete_friend(request.appId, request.wxid)

@router.post("/setFriendPermissions")
async def set_friend_permissions(request: SetFriendPermissionsRequest):
    """Set friend chat-only permissions"""
    return contact.set_friend_permissions(request.appId, request.wxid, request.onlyChat)

@router.post("/setFriendRemark")
async def set_friend_remark(request: SetFriendRemarkRequest):
    """Set friend remark/nickname"""
    return contact.set_friend_remark(request.appId, request.wxid, request.onlyChat)  # Note: onlyChat is actually remark

@router.post("/getPhoneAddressList")
async def get_phone_address_list(request: GetPhoneAddressListRequest):
    """Get phone address list"""
    return contact.get_phone_address_list(request.appId, request.wxid)  # Note: wxid is actually phones

@router.post("/uploadPhoneAddressList")
async def upload_phone_address_list(request: UploadPhoneAddressListRequest):
    """Upload phone address list"""
    return contact.upload_phone_address_list(request.appId, request.wxid, request.opType)  # Note: wxid is actually phones