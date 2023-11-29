from django.urls import path, include, re_path
from django.views.static import serve
# from app.views import LoginView, RegisterView, LogoutView, UserInfoView
from app.views import User, Product
from app import views, utils
from backend import settings

urlpatterns = [
    # user
    path("register", User.Register.as_view()),
    path("login", User.Login.as_view()),
    path("user", User.GetUserInfo.as_view()),
    path("user/avatar/update", User.AvatarUpdate.as_view()),
    path("user/basicInfor/update", User.BasicInfoUpdate.as_view()),
    path("user/defaultRecInfor/update", User.DefaultRecInforUpdate.as_view()),
    path("user/recInfor/new", User.AddRecInfor.as_view()),

    # product
    path("products", Product.GetAllProducts.as_view()),
    # path('products/<int:productId>', ),
    # path("products/posted", Product.GetPostedProducts.as_view()),
    path("product/new", Product.PostProduct.as_view()),
    path("product/comments/new", Product.AddProductComment.as_view()),


    # 访问图片
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^media/(?P<path>.*)$', utils.serve_media),
]