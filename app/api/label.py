from typing import Dict, Any, List
from app.utils.http_client import HttpClient

class LabelApi:
    @staticmethod
    async def add(app_id: str, label_name: str) -> Dict[str, Any]:
        """
        添加标签
        """
        params = {
            "appId": app_id,
            "labelName": label_name
        }
        return await HttpClient.post_json("/label/add", params)
    
    @staticmethod
    async def delete(app_id: str, label_ids: str) -> Dict[str, Any]:
        """
        删除标签
        """
        params = {
            "appId": app_id,
            "labelIds": label_ids
        }
        return await HttpClient.post_json("/label/delete", params)
    
    @staticmethod
    async def list(app_id: str) -> Dict[str, Any]:
        """
        获取标签列表
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/label/list", params)
    
    @staticmethod
    async def modify_member_list(app_id: str, label_ids: str, wx_ids: List[str]) -> Dict[str, Any]:
        """
        修改标签成员列表
        """
        params = {
            "appId": app_id,
            "labelIds": label_ids,
            "wxIds": wx_ids
        }
        return await HttpClient.post_json("/label/modifyMemberList", params)