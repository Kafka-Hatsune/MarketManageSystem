import request from '@/utils/request'

// 判断管理员权限
export const permissionJudgeAdminService = () =>
  request.get('/administractor/permission')
