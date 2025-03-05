from typing import Dict, Any, List
from app.utils.http_client import HttpClient

class GroupApi:
    @staticmethod
    async def create_chatroom(app_id: str, wxids: List[str]) -> Dict[str, Any]:
        """
        创建微信群
        """
        params = {
            "appId": app_id,
            "wxid": wxids
        }
        return await HttpClient.post_json("/group/createChatroom", params)
    
    @staticmethod
    async def modify_chatroom_name(app_id: str, chatroom_name: str, chatroom_id: str) -> Dict[str, Any]:
        """
        修改群名称
        """
        params = {
            "appId": app_id,
            "chatroomName": chatroom_name,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/modifyChatroomName", params)
    
    @staticmethod
    async def modify_chatroom_remark(app_id: str, chatroom_remark: str, chatroom_id: str) -> Dict[str, Any]:
        """
        修改群备注
        """
        params = {
            "appId": app_id,
            "chatroomRemark": chatroom_remark,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/modifyChatroomRemark", params)
    
    @staticmethod
    async def modify_chatroom_nick_name_for_self(app_id: str, nick_name: str, chatroom_id: str) -> Dict[str, Any]:
        """
        修改我在群内的昵称
        """
        params = {
            "appId": app_id,
            "nickName": nick_name,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/modifyChatroomNickNameForSelf", params)
    
    @staticmethod
    async def invite_member(app_id: str, wxids: List[str], chatroom_id: str, reason: str) -> Dict[str, Any]:
        """
        邀请/添加 进群
        """
        params = {
            "appId": app_id,
            "wxids": wxids,
            "reason": reason,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/inviteMember", params)
    
    @staticmethod
    async def remove_member(app_id: str, wxids: List[str], chatroom_id: str) -> Dict[str, Any]:
        """
        删除群成员
        """
        params = {
            "appId": app_id,
            "wxids": wxids,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/removeMember", params)
    
    @staticmethod
    async def quit_chatroom(app_id: str, chatroom_id: str) -> Dict[str, Any]:
        """
        退出群聊
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/quitChatroom", params)
    
    @staticmethod
    async def disband_chatroom(app_id: str, chatroom_id: str) -> Dict[str, Any]:
        """
        解散群聊
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/disbandChatroom", params)
    
    @staticmethod
    async def get_chatroom_info(app_id: str, chatroom_id: str) -> Dict[str, Any]:
        """
        获取群信息
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/getChatroomInfo", params)
    
    @staticmethod
    async def get_chatroom_member_list(app_id: str, chatroom_id: str) -> Dict[str, Any]:
        """
        获取群成员列表
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/getChatroomMemberList", params)
    
    @staticmethod
    async def get_chatroom_member_detail(app_id: str, chatroom_id: str, member_wxids: List[str]) -> Dict[str, Any]:
        """
        获取群成员详情
        """
        params = {
            "appId": app_id,
            "memberWxids": member_wxids,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/getChatroomMemberDetail", params)
    
    @staticmethod
    async def get_chatroom_announcement(app_id: str, chatroom_id: str) -> Dict[str, Any]:
        """
        获取群公告
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/getChatroomAnnouncement", params)
    
    @staticmethod
    async def set_chatroom_announcement(app_id: str, chatroom_id: str, content: str) -> Dict[str, Any]:
        """
        设置群公告
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id,
            "content": content
        }
        return await HttpClient.post_json("/group/setChatroomAnnouncement", params)
    
    @staticmethod
    async def agree_join_room(app_id: str, url: str) -> Dict[str, Any]:
        """
        同意进群
        """
        params = {
            "appId": app_id,
            "chatroomName": url  # Note: In the Java code this parameter is oddly named
        }
        return await HttpClient.post_json("/group/agreeJoinRoom", params)
    
    @staticmethod
    async def add_group_member_as_friend(app_id: str, member_wxid: str, chatroom_id: str, content: str) -> Dict[str, Any]:
        """
        添加群成员为好友
        """
        params = {
            "appId": app_id,
            "memberWxid": member_wxid,
            "content": content,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/addGroupMemberAsFriend", params)
    
    @staticmethod
    async def get_chatroom_qr_code(app_id: str, chatroom_id: str) -> Dict[str, Any]:
        """
        获取群二维码
        """
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/getChatroomQrCode", params)
    
    @staticmethod
    async def save_contract_list(app_id: str, oper_type: int, chatroom_id: str) -> Dict[str, Any]:
        """
        群保存到通讯录
        """
        params = {
            "appId": app_id,
            "chatroomName": oper_type,  # Note: In the Java code this parameter is oddly named
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/saveContractList", params)
    
    @staticmethod
    async def admin_operate(app_id: str, chatroom_id: str, wxids: List[str], oper_type: int) -> Dict[str, Any]:
        """
        管理员操作
        """
        params = {
            "appId": app_id,
            "wxids": wxids,
            "operType": oper_type,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/adminOperate", params)
    
    @staticmethod
    async def pin_chat(app_id: str, top: bool, chatroom_id: str) -> Dict[str, Any]:
        """
        聊天置顶
        """
        params = {
            "appId": app_id,
            "top": top,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/pinChat", params)
    
    @staticmethod
    async def set_msg_silence(app_id: str, silence: bool, chatroom_id: str) -> Dict[str, Any]:
        """
        设置消息免打扰
        """
        params = {
            "appId": app_id,
            "silence": silence,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/setMsgSilence", params)
    
    @staticmethod
    async def join_room_using_qr_code(app_id: str, qr_url: str) -> Dict[str, Any]:
        """
        扫码进群
        """
        params = {
            "appId": app_id,
            "qrUrl": qr_url
        }
        return await HttpClient.post_json("/group/joinRoomUsingQRCode", params)
    
    @staticmethod
    async def room_access_apply_check_approve(app_id: str, new_msg_id: str, chatroom_id: str, msg_content: str) -> Dict[str, Any]:
        """
        确认进群申请
        """
        params = {
            "appId": app_id,
            "newMsgId": new_msg_id,
            "msgContent": msg_content,
            "chatroomId": chatroom_id
        }
        return await HttpClient.post_json("/group/roomAccessApplyCheckApprove", params)