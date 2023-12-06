from django.views import View
from rest_framework.views import APIView, Request
from rest_framework.response import Response

from app.models import Order, User, Product, Comment
from datetime import datetime, timedelta
from app.utils import get_header_token, decode_token


class GetProductCount(APIView):
    def get(self, request):
        code, message = 200, '获取商品数量成功'
        number = Product.objects.count()
        return Response({'code': code, 'message': message, 'data': {'number': number}})


class GetActiveUserCount(APIView):
    def get(self, request):
        code, message = 200, '获取周活跃用户量成功'
        number = 0
        begin_time = datetime.now() - timedelta(days=7)
        # active_order = Order.objects.filter(create_time__gt=begin_time)
        buyer_users = Order.objects.filter(create_time__gt=begin_time).values_list('buyer_name', flat=True).distinct()
        seller_users = Order.objects.filter(create_time__gt=begin_time).values_list('seller_name', flat=True).distinct()
        poster_users = Product.objects.filter(post_time__gt=begin_time).values_list('publisher__name', flat=True).distinct()
        print(buyer_users)
        print(seller_users)
        print(poster_users)
        for u in User.objects.all():
            if u.name in buyer_users or u.name in seller_users or u.name in poster_users:
                number += 1
        return Response({'code': code, 'message': message, 'data': {'number': number}})


class GetCommentCount(APIView):
    def get(self, request):
        code, message = 200, '获取评论数量成功'
        number = Comment.objects.count()
        return Response({'code': code, 'message': message, 'data': {'number': number}})


class GetActiveOrderCount(APIView):
    def get(self, request):
        code, message = 200, '获取周交易量成功'
        begin_time = datetime.now() - timedelta(days=7)
        number = Order.objects.filter(create_time__gt=begin_time).count()
        return Response({'code': code, 'message': message, 'data': {'number': number}})

