import request from '@/utils/request'

// 给其他用户发送私信
export const messageNewService = ({ userName, content }) =>
  request.post('/message/new', { userName, content })

// 用户获取自己的未读消息
export const messageGetUnreadService = () => request.get('/message/unread/get')

// 用户获取自己的所有信息
export const messageGetAllService = () => request.get('/message/all/get')

// 用户查询自己是否有已读消息
export const messageQueryUnreadService = () =>
  request.get('/message/unread/query')
