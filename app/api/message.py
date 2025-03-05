from typing import Dict, Any, Optional
from app.utils.http_client import HttpClient

class MessageApi:
    @staticmethod
    async def post_text(app_id: str, to_wxid: str, content: str, ats: str) -> Dict[str, Any]:
        """
        发送文字消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "content": content,
            "ats": ats
        }
        return await HttpClient.post_json("/message/postText", params)
    
    @staticmethod
    async def post_file(app_id: str, to_wxid: str, file_url: str, file_name: str) -> Dict[str, Any]:
        """
        发送文件消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "fileUrl": file_url,
            "fileName": file_name
        }
        return await HttpClient.post_json("/message/postFile", params)
    
    @staticmethod
    async def post_image(app_id: str, to_wxid: str, img_url: str) -> Dict[str, Any]:
        """
        发送图片消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "imgUrl": img_url
        }
        return await HttpClient.post_json("/message/postImage", params)
    
    @staticmethod
    async def post_voice(app_id: str, to_wxid: str, voice_url: str, voice_duration: int) -> Dict[str, Any]:
        """
        发送语音消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "voiceUrl": voice_url,
            "voiceDuration": voice_duration
        }
        return await HttpClient.post_json("/message/postVoice", params)
    
    @staticmethod
    async def post_video(app_id: str, to_wxid: str, video_url: str, thumb_url: str, video_duration: int) -> Dict[str, Any]:
        """
        发送视频消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "videoUrl": video_url,
            "thumbUrl": thumb_url,
            "videoDuration": video_duration
        }
        return await HttpClient.post_json("/message/postVideo", params)
    
    @staticmethod
    async def post_link(app_id: str, to_wxid: str, title: str, desc: str, link_url: str, thumb_url: str) -> Dict[str, Any]:
        """
        发送链接消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "title": title,
            "desc": desc,
            "linkUrl": link_url,
            "thumbUrl": thumb_url
        }
        return await HttpClient.post_json("/message/postLink", params)
    
    @staticmethod
    async def post_name_card(app_id: str, to_wxid: str, nick_name: str, name_card_wxid: str) -> Dict[str, Any]:
        """
        发送名片消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "nickName": nick_name,
            "nameCardWxid": name_card_wxid
        }
        return await HttpClient.post_json("/message/postNameCard", params)
    
    @staticmethod
    async def post_emoji(app_id: str, to_wxid: str, emoji_md5: str, emoji_size: str) -> Dict[str, Any]:
        """
        发送emoji消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "emojiMd5": emoji_md5,
            "emojiSize": emoji_size
        }
        return await HttpClient.post_json("/message/postEmoji", params)
    
    @staticmethod
    async def post_app_msg(app_id: str, to_wxid: str, appmsg: str) -> Dict[str, Any]:
        """
        发送appmsg消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "appmsg": appmsg
        }
        return await HttpClient.post_json("/message/postAppMsg", params)
    
    @staticmethod
    async def post_mini_app(
        app_id: str, to_wxid: str, mini_app_id: str, display_name: str, 
        page_path: str, cover_img_url: str, title: str, user_name: str
    ) -> Dict[str, Any]:
        """
        发送小程序消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "miniAppId": mini_app_id,
            "displayName": display_name,
            "pagePath": page_path,
            "coverImgUrl": cover_img_url,
            "title": title,
            "userName": user_name
        }
        return await HttpClient.post_json("/message/postMiniApp", params)
    
    @staticmethod
    async def forward_file(app_id: str, to_wxid: str, xml: str) -> Dict[str, Any]:
        """
        转发文件
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "xml": xml
        }
        return await HttpClient.post_json("/message/forwardFile", params)
    
    @staticmethod
    async def forward_image(app_id: str, to_wxid: str, xml: str) -> Dict[str, Any]:
        """
        转发图片
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "xml": xml
        }
        return await HttpClient.post_json("/message/forwardImage", params)
    
    @staticmethod
    async def forward_video(app_id: str, to_wxid: str, xml: str) -> Dict[str, Any]:
        """
        转发视频
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "xml": xml
        }
        return await HttpClient.post_json("/message/forwardVideo", params)
    
    @staticmethod
    async def forward_url(app_id: str, to_wxid: str, xml: str) -> Dict[str, Any]:
        """
        转发链接
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "xml": xml
        }
        return await HttpClient.post_json("/message/forwardUrl", params)
    
    @staticmethod
    async def forward_mini_app(app_id: str, to_wxid: str, xml: str, cover_img_url: str) -> Dict[str, Any]:
        """
        转发小程序
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "xml": xml,
            "coverImgUrl": cover_img_url
        }
        return await HttpClient.post_json("/message/forwardMiniApp", params)
    
    @staticmethod
    async def revoke_msg(app_id: str, to_wxid: str, msg_id: str, new_msg_id: str, create_time: str) -> Dict[str, Any]:
        """
        撤回消息
        """
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "msgId": msg_id,
            "newMsgId": new_msg_id,
            "createTime": create_time
        }
        return await HttpClient.post_json("/message/revokeMsg", params)