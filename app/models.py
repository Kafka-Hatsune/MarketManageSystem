from django.db import models

EMAIL_LEN = 30
NAME_LEN = 10
PASSWD_LEN = 50
PHONE_LEN = 30
PLACE_LEN = 100
PRODUCT_MAME_LEN = 50
DESCRIPTION_LEN = 200


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=EMAIL_LEN, verbose_name='email')
    name = models.CharField(max_length=NAME_LEN, verbose_name='姓名', primary_key=True)
    password = models.CharField(max_length=PASSWD_LEN, verbose_name='密码')
    currentInfo = models.ForeignKey('UserInfo', on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='current')
    avatar = models.ForeignKey('Images', null=True, on_delete=models.SET_NULL, default=None)

    class Meta:
        db_table = 'users'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # userInfo_id = models.IntegerField()
    name = models.CharField(max_length=NAME_LEN, verbose_name='收货人姓名')
    phone = models.CharField(max_length=PHONE_LEN, verbose_name='收货人手机号')
    place = models.CharField(max_length=PLACE_LEN, verbose_name='收货地址')

    class Meta:
        db_table = 'adder_info'
        # unique_together = (("user", "userInfo_id"),)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    type = models.CharField(max_length=100)
    fatherType = models.ForeignKey('ProductType', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_type'

    def __str__(self):
        return self.type


class Product(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=PRODUCT_MAME_LEN, verbose_name='商品')
    price = models.IntegerField()
    description = models.CharField(max_length=DESCRIPTION_LEN, verbose_name='描述')
    sale = models.IntegerField(default=0)
    stock = models.IntegerField()
    post_time = models.DateTimeField(auto_now_add=True)
    product_type = models.ForeignKey(ProductType, null=True, blank=True, on_delete=models.CASCADE)

    def get_create_time(self):
        time = self.post_time.strftime('%Y-%m-%d %H:%M:%S')
        return time

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'favorite'
        unique_together = (("user", "product"),)

    def __str__(self):
        return self.user, self.product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)    # 加入购物车的时间

    def get_create_time(self):
        time = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return time

    class Meta:
        db_table = 'cart'
        unique_together = (("user", "product"),)

    def __str__(self):
        return self.user, self.product


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    # status = models.CharField()

    def get_create_time(self):
        time = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return time

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.buyer, self.product


class Comment(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def get_create_time(self):
        time = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return time

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.text


class Images(models.Model):
    img = models.ImageField(upload_to='images', default='')
    # img = models.ImageField(upload_to=get_file_path, default='')

    def get_url(self):
        img_path = "" if self.img == '' else ('http://127.0.0.1:8000/media/images/'
                                              + str(self.img.name).split('/')[-1])
        return img_path

    class Meta:
        db_table = 'images'


class ProductImages(models.Model):
    img = models.ForeignKey(Images, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'

