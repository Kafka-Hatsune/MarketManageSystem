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
export const userUpdateInfoService = (email) =>
  request.post('/user/basicInfor/update', { email })

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

// 用户获取自己的默认收货地址
export const userGetDefaultRecInforService = () =>
  request.get('/user/recInfor/default')

// 用户获取自己的所有收货地址
export const userGetAllRecInforService = () => request.get('/user/recInfors')

// 更新用户密码
export const userUpdatePasswordService = ({ old_pwd, new_pwd, re_pwd }) =>
  request.patch('/my/updatepwd', { old_pwd, new_pwd, re_pwd })

// 上传用户清单批量添加用户
export const userUploadExcelService = (file) =>
  request.post('/administractor/users/new', file, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

// 获取所有用户信息(管理员)
export const userGetAllUserService = () =>
  request.get('/administractor/user/all')

// 删除用户(管理员)
export const userDeleteUserService = ({ userName }) =>
  request.post('/administractor/user/delete', { userName })
