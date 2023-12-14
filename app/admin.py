from django.contrib import admin

from app.models import User, UserInfo, Product, ProductType, Favorite, Cart, Order, Images, Administrator

# Register your models here.
admin.site.register([User, UserInfo, Product, ProductType, Favorite, Cart, Order, Images, Administrator])

