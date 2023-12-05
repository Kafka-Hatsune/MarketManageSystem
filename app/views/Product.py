from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView, Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from app.models import User, UserInfo, Images, Product, ProductType, ProductImages, Comment, Favorite, Cart, Order
import json

from app.utils import gen_token, get_header_token, decode_token
from app.views.Util import getProductData


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
            except Product.DoesNotExist:
                code, message = -2, '评论的商品不存在'
        return Response({'code': code, 'message': message})


class GetAllProducts(APIView):
    def get(self, request):
        code, message = 200, ''  # 不检测token也可以吧
        product_list = []
        product_list_raw = Product.objects.all()
        for p in product_list_raw:
            if p.stock == 0:  # 不get库存为0的商品
                continue
            product_list.append(getProductData(p))
        return Response({'code': code, 'message': message, 'data': product_list})


class GetProduct(APIView):
    def get(self, request, product_id):
        data = {}
        try:
            p = Product.objects.get(id=product_id)
            data = getProductData(p)
            code, message = 200, '获取商品信息成功'
        except Product.DoesNotExist:
            code, message = -1, '商品不存在'
        return Response({'code': code, 'message': message, 'data': data})


class GetPostedProducts(APIView):
    def get(self, request):
        token = get_header_token(request)
        data = []
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            product_list_raw = Product.objects.filter(publisher=user)
            for p in product_list_raw:
                data.append(getProductData(p))
            code, message = 200, '成功获取用户发布的商品'
        return Response({'code': code, 'message': message, 'data': data})


class ProductModify(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)

            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                if product.publisher != user:
                    return Response({'code': -3, 'message': "用户未发布该商品"})
                productName = request.data.get('ProductName')
                if productName:
                    product.product_name = productName
                price = request.data.get('price')
                if price:
                    product.price = price
                description = request.data.get('description')
                if description:
                    product.description = description
                stock = request.data.get('stock')
                if stock:
                    product.stock = stock
                imgs = request.FILES.getlist('productPic')
                if imgs:
                    # 先把原来的图片都删了
                    oldImgs = ProductImages.objects.filter(product=product)
                    oldImgs.delete()
                    for img in imgs:
                        print(img.name)
                        # 再创建images
                        i = Images.objects.create(img=img)
                        i.save()
                        # 然后创建关联表productImages
                        product_pic = ProductImages.objects.create(img=i, product=product)
                        product_pic.save()
                product.save()
                code, message = 200, '商品信息修改成功'
            except Product.DoesNotExist:
                code, message = -2, '商品不存在'
        return Response({'code': code, 'message': message})


class ChangeStarStatus(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                if Favorite.objects.filter(user=user, product=product).count() > 0:
                    Favorite.objects.get(user=user, product=product).delete()
                else:
                    f = Favorite.objects.create(user=user, product=product)
                    f.save()
                code, message = 200, '商品收藏状态修改成功'
            except Product.DoesNotExist:
                code, message = -2, '商品不存在'
        return Response({'code': code, 'message': message})


class ProductStarSelect(APIView):
    def post(self, request):
        token = get_header_token(request)
        data = {}
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                ifStarred = (Favorite.objects.filter(user=user, product=product).count() > 0)
                data = {'ifStarred': ifStarred}
                code, message = 200, '返回收藏状态成功'
            except Product.DoesNotExist:
                code, message = -2, '查询的商品不存在'
        return Response({'code': code, 'message': message, 'data': data})


class GetStarredProducts(APIView):
    def get(self, request):
        token = get_header_token(request)
        data = []
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            favorite_list_raw = Favorite.objects.filter(user=user)
            for f in favorite_list_raw:
                data.append(getProductData(f.product))
            code, message = 200, '获取用户收藏商品成功'
        return Response({'code': code, 'message': message, 'data': data})


class GetProductTypes(APIView):
    def get(self, request):
        data = []
        typeNameList = ProductType.objects.all()
        for t in typeNameList:
            data.append({"typeName": t.type})
        code, message = 200, '获取商品种类成功'
        return Response({'code': code, 'message': message, 'data': data})


class PurchaseProduct(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                count_to_buy = request.data.get('count')
                stock = product.stock
                if count_to_buy > stock:
                    code, message = -3, '购买失败，购买商品数大于库存'
                else:
                    # 修改商品信息
                    product.stock -= count_to_buy
                    product.sale += count_to_buy
                    product.save()
                    # 创建订单
                    o = Order.objects.create(buyer=user, product=product, number=count_to_buy,
                                             buyer_name=userName,
                                             product_name=product.product_name,
                                             seller_name=product.publisher.name,
                                             price=product.price,
                                             receiver_name=user.currentInfo.name,
                                             receiver_phone=user.currentInfo.phone,
                                             receiver_place=user.currentInfo.place)
                    o.save()
                    code, message = 200, '购买成功'
            except Product.DoesNotExist:
                code, message = -2, '购买的商品不存在'
        return Response({'code': code, 'message': message})


class GetProductsInCart(APIView):
    def get(self, request):
        token = get_header_token(request)
        data = []
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            cart_list_raw = Cart.objects.filter(user=user)
            for c in cart_list_raw:
                data.append({
                    'productId': c.product.id,
                    'productName': c.product.product_name,
                    'productPic': None if not ProductImages.objects.filter(product=c.product)
                    else ProductImages.objects.filter(product=c.product)[0],
                    'price': c.product.price,
                    'count': c.count,
                    'stock': c.product.stock,
                    'createdTime': c.get_create_time(),
                })
            code, message = 200, '成功获取购物车中商品'
        return Response({'code': code, 'message': message, 'data': data})


class AddProductToCart(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                count = request.data.get('count')
                if Cart.objects.filter(user=user, product=product).count() > 0:
                    # 如果购物车中原本就有商品，则增加数量
                    c = Cart.objects.get(user=user, product=product)
                    c.count += count
                    c.save()
                else:
                    c = Cart.objects.create(user=user, product=product, count=count)
                    c.save()
                code, message = 200, '商品加入购物车成功'
            except Product.DoesNotExist:
                code, message = -2, '商品不存在'
        return Response({'code': code, 'message': message})


class DeleteProductFromCart(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                c = Cart.objects.get(user=user, product_id=productId)  # product_id的用法可以吗
                c.delete()
                code, message = 200, '从购物车删除商品成功'
            except Cart.DoesNotExist:
                code, message = -2, '购物车中不存在该商品'
        return Response({'code': code, 'message': message})


class ProductCartSelect(APIView):
    def post(self, request):
        token = get_header_token(request)
        data = {}
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                ifCart = (Cart.objects.filter(user=user, product=product).count() > 0)
                data = {'ifCart': ifCart}
                code, message = 200, '成功返回是否加购'
            except Product.DoesNotExist:
                code, message = -2, '查询的商品不存在'
        return Response({'code': code, 'message': message, 'data': data})


class CartModify(APIView):
    def post(self, request):
        token = get_header_token(request)
        if not decode_token(token):
            code, message = -1, '登录超时或者其他原因导致token失效'
        else:
            userName = decode_token(token)['username']
            user = User.objects.get(name=userName)
            productId = request.data.get('productId')
            try:
                product = Product.objects.get(id=productId)
                cartInfo = Cart.objects.get(user=user, product=product)
                count = request.data.get('count')
                cartInfo.count = count
                cartInfo.save()
                code, message = 200, '修改购物车信息成功'
            except Product.DoesNotExist:
                code, message = -2, '商品id不存在'
            except Cart.DoesNotExist:
                code, message = -3, '购物车中不存在该商品'
        return Response({'code': code, 'message': message})
