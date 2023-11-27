import request from '@/utils/request'

// 注册
export const userRegisterService = ({ userName, email, password }) =>
  request.post('/register', { userName, email, password })

// 登录
export const userLoginService = ({ userName, password }) =>
  request.post('/login', { userName, password })

// 获取用户基本信息
export const userGetInfoService = () => request.get('/user')

// 更新用户基本信息
export const userUpdateInfoService = ({ id, name, email, avatar }) =>
  request.patch('/user/update', { id, name, email, avatar })

// 更新用户头像 avatar为FormData
export const userUpdateAvatarService = (avatar) =>
  request.post('user/avatar/update', avatar, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

// 用户新建收货信息
export const userCreateRecInfoService = ({ recName, phone, place }) =>
  request.post('/user/recInfor/new', {
    name: recName,
    phone: phone,
    place: place
  })
// 用户设置默认收货信息
export const userSetDefaultRecInfoService = ({ id }) =>
  request.post('/user/defaultRecInfor/update', { id })
// 更新用户密码
export const userUpdatePasswordService = ({ old_pwd, new_pwd, re_pwd }) =>
  request.patch('/my/updatepwd', { old_pwd, new_pwd, re_pwd })
