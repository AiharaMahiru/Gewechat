from typing import Dict, Any, List
from app.utils.http_client import HttpClient

class ContactApi:
    @staticmethod
    async def check_online(app_id: str) -> Dict[str, Any]:
        """
        检查连接状态
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/login/checkOnline", params)
    
    @staticmethod
    async def fetch_contacts_list(app_id: str) -> Dict[str, Any]:
        """
        获取通讯录列表
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/contacts/fetchContactsList", params)
    
    @staticmethod
    async def get_brief_info(app_id: str, wxids: List[str]) -> Dict[str, Any]:
        """
        获取群/好友简要信息
        """
        params = {
            "appId": app_id,
            "wxids": wxids
        }
        return await HttpClient.post_json("/contacts/getBriefInfo", params)
    
    @staticmethod
    async def get_detail_info(app_id: str, wxids: List[str]) -> Dict[str, Any]:
        """
        获取群/好友详细信息
        """
        params = {
            "appId": app_id,
            "wxids": wxids
        }
        return await HttpClient.post_json("/contacts/getDetailInfo", params)
    
    @staticmethod
    async def search(app_id: str, contacts_info: str) -> Dict[str, Any]:
        """
        搜索好友
        """
        params = {
            "appId": app_id,
            "contactsInfo": contacts_info
        }
        return await HttpClient.post_json("/contacts/search", params)
    
    @staticmethod
    async def add_contacts(app_id: str, scene: int, option: int, v3: str, v4: str, content: str) -> Dict[str, Any]:
        """
        添加联系人/同意添加好友
        """
        params = {
            "appId": app_id,
            "scene": scene,
            "option": option,
            "v3": v3,
            "v4": v4,
            "content": content
        }
        return await HttpClient.post_json("/contacts/addContacts", params)
    
    @staticmethod
    async def delete_friend(app_id: str, wxid: str) -> Dict[str, Any]:
        """
        删除好友
        """
        params = {
            "appId": app_id,
            "wxid": wxid
        }
        return await HttpClient.post_json("/contacts/deleteFriend", params)
    
    @staticmethod
    async def set_friend_permissions(app_id: str, wxid: str, only_chat: bool) -> Dict[str, Any]:
        """
        设置好友仅聊天
        """
        params = {
            "appId": app_id,
            "wxid": wxid,
            "onlyChat": only_chat
        }
        return await HttpClient.post_json("/contacts/setFriendPermissions", params)
    
    @staticmethod
    async def set_friend_remark(app_id: str, wxid: str, remark: str) -> Dict[str, Any]:
        """
        设置好友备注
        """
        params = {
            "appId": app_id,
            "wxid": wxid,
            "onlyChat": remark  # Note: This is a bug in the original Java code, should be "remark"
        }
        return await HttpClient.post_json("/contacts/setFriendRemark", params)
    
    @staticmethod
    async def get_phone_address_list(app_id: str, phones: List[str]) -> Dict[str, Any]:
        """
        获取手机通讯录
        """
        params = {
            "appId": app_id,
            "wxid": phones  # Note: This is a bug in the original Java code, should be "phones"
        }
        return await HttpClient.post_json("/contacts/getPhoneAddressList", params)
    
    @staticmethod
    async def upload_phone_address_list(app_id: str, phones: List[str], op_type: int) -> Dict[str, Any]:
        """
        上传手机通讯录
        """
        params = {
            "appId": app_id,
            "wxid": phones,  # Note: This is a bug in the original Java code, should be "phones"
            "opType": op_type
        }
        return await HttpClient.post_json("/contacts/uploadPhoneAddressList", params)