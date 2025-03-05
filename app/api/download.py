from typing import Dict, Any
from app.utils.http_client import HttpClient

class DownloadApi:
    @staticmethod
    async def download_image(app_id: str, xml: str, type_: int) -> Dict[str, Any]:
        """
        下载图片
        """
        params = {
            "appId": app_id,
            "xml": xml,
            "type": type_
        }
        return await HttpClient.post_json("/message/downloadImage", params)
    
    @staticmethod
    async def download_voice(app_id: str, xml: str, msg_id: int) -> Dict[str, Any]:
        """
        下载语音
        """
        params = {
            "appId": app_id,
            "xml": xml,
            "msgId": msg_id
        }
        return await HttpClient.post_json("/message/downloadVoice", params)
    
    @staticmethod
    async def download_video(app_id: str, xml: str) -> Dict[str, Any]:
        """
        下载视频
        """
        params = {
            "appId": app_id,
            "xml": xml
        }
        return await HttpClient.post_json("/message/downloadVideo", params)
    
    @staticmethod
    async def download_emoji_md5(app_id: str, emoji_md5: str) -> Dict[str, Any]:
        """
        下载emoji
        """
        params = {
            "appId": app_id,
            "emojiMd5": emoji_md5
        }
        return await HttpClient.post_json("/message/downloadEmojiMd5", params)
    
    @staticmethod
    async def download_cdn(app_id: str, aes_key: str, file_id: str, type_: str, total_size: str, suffix: str) -> Dict[str, Any]:
        """
        cdn下载
        """
        params = {
            "appId": app_id,
            "aesKey": aes_key,
            "fileId": file_id,
            "totalSize": total_size,
            "type": type_,
            "suffix": suffix
        }
        return await HttpClient.post_json("/message/downloadCdn", params)