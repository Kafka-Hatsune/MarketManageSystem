import axios from 'axios'
import { useUserStore } from '@/stores'
import router from '@/router'
import { ElMessage } from 'element-plus'

const baseURL = 'http://127.0.0.1:4523/m1/3576156-0-default'
// const baseURL = 'http://127.0.0.1:8000/'
// 创建一个新的axios实例
const instance = axios.create({
  baseURL, // 基础地址
  timeout: 10000 // 超时时间 10s
})

// 新实例instance的请求拦截器
instance.interceptors.request.use(
  (config) => {
    // 请求携带token时填充请求头的Authorization
    const useStore = useUserStore()
    if (useStore.token) {
      config.headers.Authorization = 'Bearer ' + useStore.token
    }
    return config
  },
  (err) => Promise.reject(err)
)

// 新实例instance的响应拦截器
instance.interceptors.response.use(
  (res) => {
    console.log('经过了响应拦截器')
    // 200 OK
    if (res.data.code === 200) {
      return res
    }
    // 处理业务失败, 给错误提示，抛出错误
    ElMessage.error(res.data.message || '服务异常')
    return Promise.reject(res.data)
  },
  (err) => {
    // 401 权限不足 或 token 过期 => 拦截到登录
    if (err.response?.status === 401) {
      router.push('/login')
    }

    // 错误的默认情况 => 只要给提示
    ElMessage.error(err.response.data.message || '服务异常')
    return Promise.reject(err)
  }
)
// 将修改好的axios实例导出
export default instance
export { baseURL }
