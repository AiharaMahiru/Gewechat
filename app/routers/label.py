from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List
from app.api import label

router = APIRouter(prefix="/label", tags=["label"])

# Models for request validation
class AddLabelRequest(BaseModel):
    appId: str
    labelName: str

class DeleteLabelRequest(BaseModel):
    appId: str
    labelIds: str

class ListLabelsRequest(BaseModel):
    appId: str

class ModifyMemberListRequest(BaseModel):
    appId: str
    labelIds: str
    wxIds: List[str]

# Endpoint implementations
@router.post("/add")
async def add_label(request: AddLabelRequest):
    """Add a label"""
    return label.add(request.appId, request.labelName)

@router.post("/delete")
async def delete_label(request: DeleteLabelRequest):
    """Delete a label"""
    return label.delete(request.appId, request.labelIds)

@router.post("/list")
async def list_labels(request: ListLabelsRequest):
    """List all labels"""
    return label.list(request.appId)

@router.post("/modifyMemberList")
async def modify_member_list(request: ModifyMemberListRequest):
    """Modify label member list"""
    return label.modify_member_list(request.appId, request.labelIds, request.wxIds)