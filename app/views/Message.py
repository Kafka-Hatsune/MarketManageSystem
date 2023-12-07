from rest_framework.views import APIView, Request
from rest_framework.response import Response
from app.models import User, Message

from app.utils import get_header_token, decode_token


class SendMessage(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            recipient_name = request.data.get('userName')
            content = request.data.get('content')
            try:
                recipient_user = User.objects.get(name=recipient_name)
                m = Message.objects.create(sender=user, recipient=recipient_user,
                                           senderName=userName, recipient_name=recipient_name,
                                           content=content)
                m.save()
                code, message = 200, '消息发送成功'
            except User.DoesNotExist:
                code, message = -2, '发送失败，接收者不存在'
        return Response({'code': code, 'message': message})


class GetUnreadMessage(APIView):
    def get(self, request):
        data = []
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            message_unread_list = Message.objects.filter(recipient=user, status='unread')
            for m in message_unread_list:
                data.append({
                    'sender': {
                        'userName': m.senderName
                    },
                    'content': m.content
                })
                m.status = 'read'
                m.save()
            code, message = 200, '获取未读消息成功'
        return Response({'code': code, 'message': message, 'data': data})


class GetAllMessage(APIView):
    def get(self, request):
        data = []
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            message_unread_list = Message.objects.filter(recipient=user)
            for m in message_unread_list:
                data.append({
                    'sender': {
                        'userName': m.senderName
                    },
                    'content': m.content
                })
                m.status = 'read'
                m.save()
            code, message = 200, '获取所有消息成功'
        return Response({'code': code, 'message': message, 'data': data})


class UnreadMessageQuery(APIView):
    def get(self, request):
        data = []
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            message_unread_list = Message.objects.filter(recipient=user, status='unread')
            ifHas = (message_unread_list.count() > 0)
            code, message = 200, '查询用户是否有未读消息成功'
            return Response({'code': code, 'message': message, 'data': {'ifHas': ifHas}})

