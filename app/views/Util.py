import os

import openpyxl
import xlrd
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files import File
from PIL import Image

from app.models import Product, Comment, ProductImages, Images, User, Order


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


# 未使用，探索中
class DownloadFile(APIView):
    def post(self, request):
        # 创建工作簿
        wb = xlwt.Workbook()
        # 添加工作表
        sheet = wb.add_sheet('商品信息表')
        # 查询所有用户的信息
        queryset = User.objects.all()
        # 向Excel表单中写入表头
        colnames = ('商品名', '商品类型名', '价格', '库存', '销量')
        for index, name in enumerate(colnames):
            sheet.write(0, index, name)
        # 向单元格中写入商品的数据
        props = ('name', 'detail', 'good_count', 'bad_count', 'subject')
        for row, teacher in enumerate(queryset):
            for col, prop in enumerate(props):
                value = getattr(teacher, prop, '')
                if isinstance(value, Subject):
                    value = value.name
                sheet.write(row + 1, col, value)
        # 保存Excel
        buffer = BytesIO()
        wb.save(buffer)
        # 将二进制数据写⼊响应的消息体中并设置MIME类型
        resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.msexcel')
        # 中文文件名需要处理成百分号编码
        filename = quote('老师.xls')
        # 通过响应头告知浏览器下载该⽂件以及对应的文件名
        resp['content-disposition'] = f'attachment; filename*=utf-8''{filename}'
        return resp


# 未使用，探索中
class UploadFile(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            code, message = -1, '没有文件'
        # 处理Excel文件
        wb = openpyxl.load_workbook(file)
        sheet = wb.active
        i = 0
        for row in sheet.iter_rows(min_row=2):
            print(row[0].value)
            print(row[1].value)
            print(row[2].value)
            print(row[3].value)
            print(row[4].value)

            image = sheet._images[i]
            i = i + 1

            image_data = image._data()  # 获取图像数据
            # 创建临时文件路径
            temp_image_path = 'image.jpg'

            # 将图像数据保存为临时文件
            with open(temp_image_path, 'wb') as temp_image_file:
                temp_image_file.write(image_data)
            # 打开临时图像文件
            pil_image = Image.open(temp_image_path)

            # 保存调整后的图像
            pil_image.save(temp_image_path)

            with open(temp_image_path, 'rb') as image_file:
                # 创建Django的File对象
                django_file = File(image_file)

                # 将图像文件保存到ImageField对象
                im = Images.objects.create(img=django_file)
                im.save()

                # mymodel.image_field.save('image.jpg', django_file)

            # 删除临时图像文件
            os.remove(temp_image_path)

            # 创建Django模型实例
            # MyModel.objects.create(name=name, age=age, picture=picture_file)

        # file = request.FILES.get("file")
        # if not file:
        #     code, message = -1, '没有文件'
        # file_path = handle_uploaded_file(file)
        # workbook = xlrd.open_workbook(file)
        # worksheet = workbook.sheet_by_index(0)  # 假设选择第一个工作表
        #
        # for row in range(worksheet.nrows):
        #     for col in range(worksheet.ncols):
        #         cell = worksheet.cell(row, col)
        #
        #         # 检查单元格是否包含图片
        #         if cell.ctype == xlrd.XL_CELL_BLANK:
        #             continue
        #
        #         # 将图片数据存储到模型对象中
        #         image_data = cell.value  # 获取图片数据
        #
        #         # 创建模型对象并保存
        #         img = Images.objects.create(img=image_data)
        #         img.save()
        return Response({'code': 0, 'message': "finish"})
