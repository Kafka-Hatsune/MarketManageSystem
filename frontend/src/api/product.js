import request from '@/utils/request'

export const productsService = () => request.get('/products')
