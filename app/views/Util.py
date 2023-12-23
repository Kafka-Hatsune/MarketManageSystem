import os

import openpyxl
import xlrd
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files import File
from PIL import Image

from app.models import Product, Comment, ProductImages, Images, User, Order, Administrator


def getProductData(p: Product):
    data = {
        'typeName': p.product_type.type,
        'productId': p.id,
        'productName': p.product_name,
        'price': p.price,
        'description': p.description,
        'sale': p.sale,
        'stock': p.stock,
        'createdTime': p.get_create_time(),
        'productPic': [pi.img.get_url() for pi in ProductImages.objects.filter(product=p)],
        'comments': [{
            'id': c.id,
            'text': c.text,
            'createdTime': c.get_create_time(),
            'publisher': {
                'userName': c.publisher.name,
                'avatar': None if not c.publisher.avatar else c.publisher.avatar.get_url()
            },
        } for c in Comment.objects.filter(item=p)],
    }
    return data


def createOrder(user: User, product: Product, count_to_buy: int):
    stock = product.stock
    if count_to_buy > stock:
        code, message = -3, product.product_name + '购买失败，库存不足'
    elif user.currentInfo is None:
        code, message = -4, '购买失败，请先设置默认收货地址'
    else:
        # 修改商品信息
        product.stock -= count_to_buy
        product.sale += count_to_buy
        product.save()
        # 创建订单
        o = Order.objects.create(buyer=user, product=product, number=count_to_buy,
                                 buyer_name=user.name,
                                 product_name=product.product_name,
                                 seller_name=product.publisher.name,
                                 price=product.price,
                                 receiver_name=user.currentInfo.name,
                                 receiver_phone=user.currentInfo.phone,
                                 receiver_place=user.currentInfo.place)
        o.save()
        code, message = 200, '购买成功'
    return code, message


def judgeAdministrator(userName):
    user = User.objects.get(name=userName)
    print(user.name)
    return Administrator.objects.filter(user=user).count() > 0


