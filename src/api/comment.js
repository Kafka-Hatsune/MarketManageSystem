import request from '@/utils/request'

// 提交评论内容
export const commentSubmitService = ({ commentText, productId }) =>
  request.post('/product/comments/new', { commentText, productId })
