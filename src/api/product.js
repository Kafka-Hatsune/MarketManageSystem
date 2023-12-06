import request from '@/utils/request'
// 注意箭头函数加了括号记得return

// 获取所有商品的简略信息
export const productGetAllInfoService = () => request.get('/products')

// 获取一个商品的商品详情
export const productGetProductDetailService = (id) =>
  request.get(`/products/${id}`)

// 当前用户购买商品
export const productPurchaseService = ({ productId, count }) =>
  request.post('/products/purchase', { productId, count })

// 获取当前可用的商品种类
export const productGetTypeService = () => request.get('/productTypes')

// 用户创建新商品
export const productCreateService = (formdata) =>
  request.post('/product/new', formdata, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

// 用户获取自己发布的所有商品
export const productGetPostedService = () => request.get('/products/posted')

// 用户修改自己的商品信息
export const productModifyService = (formdata) =>
  request.post('/product/modify', formdata, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

// 获取用户收藏商品信息
export const productGetStarService = () => request.get('/product/star')

// 用户切换收藏商品的状态
export const productStarNewService = (id) =>
  request.post('/product/star/switch', { productId: id })

// 查询用户是否收藏该商品
export const productIfStarService = (id) =>
  request.post('/product/star/select', { productId: id })

// 获取用户购物车中所有商品信息
export const productGetCartService = () => request.get('/product/cart')

// 用户修改购物车数量信息
export const productCartCountService = ({ productId, count }) =>
  request.post('/product/cart/modify', { productId, count })

// 用户将对应商品项加入购物车
export const productCartNewService = ({ productId, count }) =>
  request.post('/product/cart/new', { productId, count })

// 用户删除购物车项
export const productCartDeleteService = (productId) =>
  request.post('/product/cart/delete', { productId })

// 查询用户购物车中是否存在该商品
export const productCartSelectService = (productId) =>
  request.post('/product/cart/select', { productId })
