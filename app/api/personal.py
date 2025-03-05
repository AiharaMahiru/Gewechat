from typing import Dict, Any
from app.utils.http_client import HttpClient

class PersonalApi:
    @staticmethod
    async def get_profile(app_id: str) -> Dict[str, Any]:
        """
        获取个人资料
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/personal/getProfile", params)
    
    @staticmethod
    async def get_qr_code(app_id: str) -> Dict[str, Any]:
        """
        获取自己的二维码
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/personal/getQrCode", params)
    
    @staticmethod
    async def get_safety_info(app_id: str) -> Dict[str, Any]:
        """
        获取设备记录
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/personal/getSafetyInfo", params)
    
    @staticmethod
    async def privacy_settings(app_id: str, option: int, open: bool) -> Dict[str, Any]:
        """
        隐私设置
        """
        params = {
            "appId": app_id,
            "option": option,
            "open": open
        }
        return await HttpClient.post_json("/personal/privacySettings", params)
    
    @staticmethod
    async def update_profile(
        app_id: str, city: str, country: str, nick_name: str, 
        province: str, sex: str, signature: str
    ) -> Dict[str, Any]:
        """
        修改个人信息
        """
        params = {
            "appId": app_id,
            "city": city,
            "country": country,
            "nickName": nick_name,
            "province": province,
            "sex": sex,
            "signature": signature
        }
        return await HttpClient.post_json("/personal/updateProfile", params)
    
    @staticmethod
    async def update_head_img(app_id: str, head_img_url: str) -> Dict[str, Any]:
        """
        修改头像
        """
        params = {
            "appId": app_id,
            "headImgUrl": head_img_url
        }
        return await HttpClient.post_json("/personal/updateHeadImg", params)