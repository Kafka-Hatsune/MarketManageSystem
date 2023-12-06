from django.urls import path, include, re_path
from django.views.static import serve

from app.views import User, Product, Util, Order, Administractor, Statistic
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
    path("user/recInfor/default", User.GetDefaultRecInfor.as_view()),
    path("user/recInfors", User.GetAllRecInfors.as_view()),

    # 商品
    path("products", Product.GetAllProducts.as_view()),
    path("products/<int:product_id>", Product.GetProduct.as_view()),
    path("products/posted", Product.GetPostedProducts.as_view()),
    path("product/new", Product.PostProduct.as_view()),
    path("product/modify", Product.ProductModify.as_view()),
    path("product/comments/new", Product.AddProductComment.as_view()),
    path("productTypes", Product.GetProductTypes.as_view()),
    path("products/purchase", Product.PurchaseProduct.as_view()),
    # 商品 收藏夹
    path("product/star/switch", Product.ChangeStarStatus.as_view()),
    path("product/star/select", Product.ProductStarSelect.as_view()),
    path("product/star", Product.GetStarredProducts.as_view()),
    # 商品 购物车
    path("product/cart", Product.GetProductsInCart.as_view()),
    path("product/cart/new", Product.AddProductToCart.as_view()),
    path("product/cart/delete", Product.DeleteProductFromCart.as_view()),
    path("product/cart/select", Product.ProductCartSelect.as_view()),
    path("product/cart/modify", Product.CartModify.as_view()),

    # 订单
    path("order/consumer", Order.GetPurchaseOrder.as_view()),
    path("order/seller", Order.GetSellOrder.as_view()),
    path("order/state/modify", Order.OrderStateModify.as_view()),

    # 管理员
    path("administractor/permission", Administractor.GetIfAdmin.as_view()),
    path("administractor/user/all", Administractor.GetAllUsers.as_view()),
    path("administractor/order/all", Administractor.GetAllOrders.as_view()),
    path("administractor/user/delete", Administractor.DeleteUser.as_view()),
    path("administractor/order/delete", Administractor.DeleteOrder.as_view()),
    path("administractor/users/new", Administractor.UploadUsers.as_view()),

    # 统计
    path("product/count", Statistic.GetProductCount.as_view()),
    path("user/active/count", Statistic.GetActiveUserCount.as_view()),
    path("comment/count", Statistic.GetCommentCount.as_view()),
    path("order/active/count", Statistic.GetActiveOrderCount.as_view()),


    # test
    # path("uploadfile", Util.UploadFile.as_view()),

    # 访问图片
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^media/(?P<path>.*)$', utils.serve_media),
]