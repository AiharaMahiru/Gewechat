from typing import Dict, Any
from app.utils.http_client import HttpClient

class FavorApi:
    @staticmethod
    async def sync(app_id: str, sync_key: str) -> Dict[str, Any]:
        """
        同步收藏夹
        """
        params = {
            "appId": app_id,
            "syncKey": sync_key
        }
        return await HttpClient.post_json("/favor/sync", params)
    
    @staticmethod
    async def get_content(app_id: str, fav_id: int) -> Dict[str, Any]:
        """
        获取收藏夹内容
        """
        params = {
            "appId": app_id,
            "favId": fav_id
        }
        return await HttpClient.post_json("/favor/getContent", params)
    
    @staticmethod
    async def delete(app_id: str, fav_id: int) -> Dict[str, Any]:
        """
        删除收藏夹
        """
        params = {
            "appId": app_id,
            "favId": fav_id
        }
        return await HttpClient.post_json("/favor/delete", params)