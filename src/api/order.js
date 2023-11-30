import request from '@/utils/request'
// 注意箭头函数加了括号记得return

// 获取用户购物车中所有商品信息
export const orderGetSeller = () => request.get('/order/seller')
export const orderGetConsumer = () => request.get('/order/consumer')
