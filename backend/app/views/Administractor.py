from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView, Request
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

# class AddUser(APIView):
#     def post(self, request : Request):
#         print(request.data)
#
#         name = str(request.data.get('name'))
#         email = str(request.data.get('email'))
#         password = str(request.data.get('password'))
#
#         ret = 200
#         reason = ''
#         # if checkEmail(email) == 1:
#         if 0 == 1:
#             ret = 1
#             reason = '邮箱已注册'
#         else:
#             try:
#                 s = Users.objects.create(
#                     email=email,
#                     name=name,
#                     password=password
#                 )
#                 s.save()
#             except Exception as e:
#                 print(e)
#                 ret = 2
#                 reason = '未知原因'
#         return Response({'value': ret, 'reason': reason})

# class RegisterView(View):
#     def post(self, request : Request):
#         request_json = json.loads(request.body)
#         name = str(request.data.get('name'))
#         email = str(request.data.get('email'))
#         password = str(request.data.get('password'))
#
#         if not name or not password:
#             result = {"code": -1, "msg": "username or password not valid"}
#         else:
#             if User.objects.filter(username=username).exists():
#                 result = {"code": -1, "msg": "username exists"}
#             else:
#                 User.objects.create(username=username, password=make_password(password))
#                 result = {"code": 0, "msg": "success"}
#         return JsonResponse(result, safe=False)