from typing import Dict, Any
from app.utils.http_client import HttpClient

class LoginApi:
    @staticmethod
    async def get_token() -> Dict[str, Any]:
        """
        获取tokenId 将tokenId 配置到HttpClient 类中的token 属性
        """
        return await HttpClient.post_json("/tools/getTokenId", {})
    
    @staticmethod
    async def set_callback(token: str, callback_url: str) -> Dict[str, Any]:
        """
        设置微信消息的回调地址
        """
        params = {
            "token": token,
            "callbackUrl": callback_url
        }
        return await HttpClient.post_json("/tools/setCallback", params)
    
    @staticmethod
    async def get_qr(app_id: str) -> Dict[str, Any]:
        """
        获取登录二维码
        
        Args:
            app_id: 设备id 首次登录传空，后续登录传返回的appid
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/login/getLoginQrCode", params)
    
    @staticmethod
    async def check_qr(app_id: str, uuid: str, captch_code: str) -> Dict[str, Any]:
        """
        确认登陆
        
        Args:
            app_id: 应用ID
            uuid: 取码返回的uuid
            captch_code: 登录验证码（跨省登录会出现此提示，使用同省代理ip能避免此问题，也能使账号更加稳定）
        """
        params = {
            "appId": app_id,
            "uuid": uuid,
            "captchCode": captch_code
        }
        return await HttpClient.post_json("/login/checkLogin", params)
    
    @staticmethod
    async def log_out(app_id: str) -> Dict[str, Any]:
        """
        退出微信
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/login/logout", params)
    
    @staticmethod
    async def dialog_login(app_id: str) -> Dict[str, Any]:
        """
        弹框登录
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/login/dialogLogin", params)
    
    @staticmethod
    async def check_online(app_id: str) -> Dict[str, Any]:
        """
        检查是否在线
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/login/checkOnline", params)
    
    @staticmethod
    async def logout(app_id: str) -> Dict[str, Any]:
        """
        退出
        """
        params = {
            "appId": app_id
        }
        return await HttpClient.post_json("/login/logout", params)