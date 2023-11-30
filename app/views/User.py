from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView, Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from app.models import User, UserInfo, Images
import json

from app.utils import gen_token, get_header_token, decode_token


# 用户注册
class Register(APIView):
    def post(self, request):
        # request_json = json.loads(request.body)
        name = str(request.data.get('userName'))
        email = str(request.data.get('email'))
        password = str(request.data.get('password'))

        if not password or not name:
            result = {"code": -1, "msg": "username or password not valid"}
        else:
            if User.objects.filter(name=name).exists():
                result = {"code": -2, "msg": "name exists"}
            else:
                User.objects.create(name=name, email=email, password=password)
                result = {"code": 200, "msg": "register success"}
        return Response(result)


# 用户登录
class Login(APIView):
    def post(self, request):
        # request_json = json.loads(request.body)
        username = str(request.data.get('userName'))
        password = str(request.data.get('password'))
        token = ''

        if not username or not password:
            result = {"code": -1, "message": "login info error"}
        else:
            user = User.objects.filter(name=username).first()
            if not user:
                result = {"code": -2, "message": "username not found"}
            else:
                if password == user.password:
                    result = {"code": 200, "message": "login success"}
                    # request.session["username"] = username
                    token = gen_token(username)
                else:
                    result = {"code": -3, "message": "password error"}
        result["data"] = {"token": token}
        return Response(result)


# 用户登出
'''
class LogoutView(APIView):
    def post(self, request):
        if request.session.get("username"):
            del request.session["username"]
            # request.session.flush()
        return Response({"code": 0, "msg": "登出成功"})
'''


# 获取用户信息
class GetUserInfo(APIView):
    def get(self, request):
        token = get_header_token(request)
        print(token)
        # msg, code = '', 0
        ret = {}

        if not decode_token(token):
            code, msg = -1, '登录超时或者其他原因导致token失效'
        else:
            username = decode_token(token)['username']
            print(username)
            code = 200
            msg = f"登录用户为{username}"

            user = User.objects.get(name=username)
            # img_path = "" if not user.avatar else user.avatar.get_url()
            img_path = None if not user.avatar else user.avatar.get_url()

            data = {
                # "id": user.id,
                "userName": username,
                "email": user.email,
                "avatar": img_path
            }
            if user.currentInfo:
                rec_info = {
                    "id": user.currentInfo.id,
                    "name": user.currentInfo.name,
                    "phone": user.currentInfo.phone,
                    "place": user.currentInfo.place
                }
                data["recInfo"] = rec_info
            else:
                data["recInfo"] = None

            all_infos = []
            infos = UserInfo.objects.filter(user=user)
            for info in infos:
                all_infos.append(
                    {
                        "id": info.id,
                        "name": info.name,
                        "phone": info.phone,
                        "place": info.place
                    }
                )
            data["recInfos"] = all_infos
            ret["data"] = data

        ret["code"] = code
        ret["message"] = msg

        return Response(ret)


class AvatarUpdate(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            username = decode_token(token)['username']
            user = User.objects.get(name=username)

            file_obj = request.FILES.get('avatar')
            print(file_obj.name)
            img = Images.objects.create(
                img=file_obj
            )
            img.save()
            user.avatar = img
            user.save()
            print(img.get_url())
            code, message = 200, '0'

        return Response({'code': code, 'message': message})


class BasicInfoUpdate(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            '''
            newName = request.data.get("userName")
            if not newName:
                u = User.objects.filter(name = newName)
                if u.exists():
                    code, message = -2, '更改失败，用户名已经存在'
                else:
                    user.name = newName
            '''

            email = request.data.get("email")
            if email is not None:
                user.email = email
                user.save()
            code, message = 200, '更改成功'
        return Response({'code': code, 'message': message})


class DefaultRecInforUpdate(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            userInfo_id = request.data.get("id")
            try:
                userInfo = UserInfo.objects.get(id=userInfo_id)
                user.currentInfo = userInfo
                user.save()
                code, message = 200, '设置成功'
            except UserInfo.DoesNotExist:
                code, message = -2, '收货信息不存在'
        return Response({'code': code, 'message': message})


class AddRecInfor(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            name = request.data.get("name")
            phone = request.data.get("phone")
            place = request.data.get("place")
            u = UserInfo.objects.create(
                user=user,
                name=name,
                phone=phone,
                place=place
            )
            u.save()
            code, message = 200, '添加成功'
        return Response({'code': code, 'message': message})

