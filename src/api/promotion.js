import request from '@/utils/request'

// 用户请求推广自己的商品
export const promotionNewService = ({ productId }) =>
  request.post('/promotion/new', { productId })

// 管理员接受推广申请
export const promotionUpdateService = ({ productId }) =>
  request.post('/promotion/update', { productId })

// 管理员拒绝推广申请并发信
export const promotionDeleteService = ({ productId }) =>
  request.post('/promotion/delete', { productId })

// 管理员获取推广申请列表
export const promotionGetAllService = () => request.get('/promotion/get')

// 获取当前的推广申请列表
export const promotionGetActiveService = () => request.get('/promotion/active')
