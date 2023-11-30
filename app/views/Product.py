from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView, Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from app.models import User, UserInfo, Images, Product, ProductType, ProductImages, Comment
import json

from app.utils import gen_token, get_header_token, decode_token


class PostProduct(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            typeName = request.data.get('typeName')
            productName = request.data.get('productName')
            price = request.data.get('price')
            description = request.data.get('description')
            stock = request.data.get('stock')

            productType = ProductType.objects.filter(type=typeName)
            if not productType:
                code, message = -2, '该商品种类不存在'
            else:
                # 先创建product
                product = Product.objects.create(
                    publisher=user,
                    product_name=productName,
                    price=price,
                    description=description,
                    stock=stock,
                    product_type=productType[0]
                )
                product.save()
                productPics = request.FILES.getlist('productPic')
                for img in productPics:
                    print(img.name)
                    # 再创建images
                    i = Images.objects.create(
                        img=img
                    )
                    i.save()
                    # 然后创建关联表productImages
                    product_pic = ProductImages.objects.create(
                        img=i,
                        product=product
                    )
                    product_pic.save()
                code, message = 200, '商品发布成功'
        return Response({'code': code, 'message': message})


'''
class GetALLProducts(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
'''


class AddProductComment(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            productId = request.data.get('productId')
            text = request.data.get('commentText')
            try:
                product = Product.objects.get(id=productId)
                c = Comment.objects.create(publisher=user, item=product, text=text)
                c.save()
                code, message = 200, '添加评论成功'
            except UserInfo.DoesNotExist:
                code, message = -2, '商品不存在'
        return Response({'code': code, 'message': message})


class GetAllProducts(APIView):
    def get(self, request):
        code, message = 200, ''        # 不检测token也可以吧
        product_list = []
        product_list_raw = Product.objects.all()
        for p in product_list_raw:
            if p.stock == 0:
                continue
            product_list.append(
                {
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
                            # 'id': c.publisher.id,
                            'userName': c.publisher.name,
                            'avatar': None if not p.publisher.avatar else p.publisher.avatar.get_url()
                        },
                    } for c in Comment.objects.filter(item=p)],
                }
            )
        return Response({'code': code, 'message': message, 'data': product_list})

