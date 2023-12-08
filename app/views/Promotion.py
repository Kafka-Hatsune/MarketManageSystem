from rest_framework.views import APIView, Request
from rest_framework.response import Response
from app.models import User, Message, Product, Promotion, ProductImages
from datetime import datetime, timedelta

from app.utils import get_header_token, decode_token
from app.views.Util import getProductData


class RequestPromotion(APIView):
    def post(self, request):
        code, message = 200, '成功申请推广'
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                promotion_list = Promotion.objects.filter(applicant=user)
                valid_count = 0
                for p in promotion_list:
                    if not p.is_checked or p.get_end_time() > datetime.now():
                        if p.product.id == productId:
                            code, message = -3, '不能重复推广该商品'
                            break
                        valid_count += 1
                        if valid_count == 3:
                            code, message = -4, '您已经推广三个商品'
                            break
                if code == 200:
                    p = Promotion.objects.create(applicant=user, product=product)
                    p.save()
            except Product.DoesNotExist:
                code, message = -2, '推广的商品不存在'
        return Response({'code': code, 'message': message})


class ReceivePromotion(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            if userName != 'Admin':
                code, message = -2, '您不是管理员，无权限进行此操作'
            else:
                productId = request.data.get('productId')
                print(productId)
                promotion = Promotion.objects.filter(product_id=productId)
                if promotion:
                    p = promotion[0]
                    p.is_checked = True
                    p.begin_time = datetime.now()
                    p.save()
                    # 向申请者发消息
                    content = "您好，您对 " + p.product.product_name + " 商品的推广申请审核通过，已经开始推广"
                    m = Message.objects.create(sender=user, recipient=p.applicant,
                                               senderName=userName, recipientName=p.applicant.name,
                                               content=content)
                    code, message = 200, '接受推广成功，开始推广'
                else:
                    code, message = -3, '推广申请或商品不存在'
        return Response({'code': code, 'message': message})


class RejectPromotion(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            if userName != 'Admin':
                code, message = -2, '您不是管理员，无权限进行此操作'
            else:
                productId = request.data.get('productId')
                promotion = Promotion.objects.filter(product_id=productId, is_checked=False)
                if promotion:
                    p = promotion[0]
                    # 向申请者发消息
                    content = "对不起，您对 " + p.product.product_name + " 商品推广申请被拒绝"
                    m = Message.objects.create(sender=user, recipient=p.applicant,
                                               senderName=userName, recipientName=p.applicant.name,
                                               content=content)
                    m.save()
                    p.delete()
                    code, message = 200, '拒绝推广成功'
                else:
                    code, message = -3, '推广申请或商品不存在'
        return Response({'code': code, 'message': message})


class GetUncheckedPromotion(APIView):
    def get(self, request):
        data = []
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            if userName != 'Admin':
                code, message = -2, '您不是管理员，无权限进行此操作'
            else:
                promotion_list = Promotion.objects.filter(is_checked=False)
                for p in promotion_list:
                    data.append({
                        'id': p.id,
                        'applicant': {
                            'userName': p.applicant.name,
                        },
                        'productId': p.product.id,
                    })
                code, message = 200, '获取推广申请成功'
        return Response({'code': code, 'message': message, 'data': data})


class GetActivePromotion(APIView):
    def get(self, request):
        code, message = 200, '获取当前推广商品列表成功'
        data = []

        promotion_list = Promotion.objects.filter(is_checked=True)
        for prom in promotion_list:
            if prom.get_end_time() > datetime.now():
                data.append(getProductData(prom.product))
        return Response({'code': code, 'message': message, 'data': data})

