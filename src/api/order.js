import request from '@/utils/request'
// 注意箭头函数加了括号记得return

// 获取用户购物车中所有商品信息
export const orderGetSeller = () => request.get('/order/seller')
export const orderGetConsumer = () => request.get('/order/consumer')

// 获取所有订单信息
export const orderGetAllService = () => request.get('/admin/order/all')

// 修改订单状态
export const orderChangeStateService = ({ id, state }) =>
  request.post('/order/state/modify', { id, state })

// 管理员删除订单
export const orderDeleteOrderService = ({ id }) =>
  request.post('/admin/order/delete', { id })
