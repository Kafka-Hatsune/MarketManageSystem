import request from '@/utils/request'

// 获取当前活跃用户数
export const statisticGetActiveUserService = () =>
  request.get('/user/active/count')

// 获取当前在售商品
export const statisticGetProductCountService = () =>
  request.get('/product/count')

// 获取当前评论总数
export const statisticGetCommentCountService = () =>
  request.get('/comment/count')

// 获取当前活跃订单
export const statisticGetActiveOrderCountService = () =>
  request.get('/order/active/count')
