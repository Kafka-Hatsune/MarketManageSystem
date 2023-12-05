from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User, Order
from app.utils import get_header_token, decode_token


class GetPurchaseOrder(APIView):
    def get(self, request):
        token = get_header_token(request)
        data = []
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            order_list_raw = Order.objects.filter(buyer=user)
            for o in order_list_raw:
                data.append({
                    'id': o.id,
                    'product': {
                        'productName': o.product.product_name,
                        'price': o.price
                    },
                    'number': o.number,
                    'status': o.status,
                    'createdTime': o.get_create_time(),
                    # 'seller': {
                    #     'userName': o.product.publisher.name
                    # },
                    'buyerInfo': {
                        'name': o.receiver_name,
                        'phone': o.receiver_phone,
                        'place': o.receiver_place
                    }
                })
            code, message = 200, '成功所有购买订单'
        return Response({'code': code, 'message': message, 'data': data})


class GetSellOrder(APIView):
    def get(self, request):
        token = get_header_token(request)
        data = []
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            order_list_raw = Order.objects.filter(product__publisher=user)
            for o in order_list_raw:
                data.append({
                    'id': o.id,
                    'buyer': {
                        'userName': o.buyer.name
                    },
                    'product': {
                        'productName': o.product_name,
                        'price': o.price
                    },
                    'number': o.number,
                    'status': o.status,
                    'createdTime': o.get_create_time(),
                    'buyerInfo': {
                        'name': o.receiver_name,
                        'phone': o.receiver_phone,
                        'place': o.receiver_place
                    }
                })
            code, message = 200, '成功所有购买订单'
        return Response({'code': code, 'message': message, 'data': data})


class OrderStateModify(APIView):
    def post(self, request):
        token = get_header_token(request)
        data = []
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            order_id = request.data.get('id')
            state = request.data.get('state')
            try:
                order = Order.objects.get(id=order_id)
                order.status = state
                order.save()
                code, message = 200, '订单状态修改成功'
            except Order.DoesNotExist:
                code, message = -2, '订单不存在'
        return Response({'code': code, 'message': message})


