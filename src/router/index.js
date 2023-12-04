import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores'
import { permissionJudgeAdminService } from '@/api/permission'
import { ElMessage } from 'element-plus'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      component: () => import('@/views/login/LoginPage.vue')
    },
    {
      path: '/',
      component: () => import('@/views/layout/LayoutContainer.vue'),
      redirect: '/home',
      children: [
        {
          path: '/home',
          component: () => import('@/views/home/HomePage.vue')
        },
        {
          path: '/user/profile',
          component: () => import('@/views/user/UserProfile.vue')
        },
        {
          path: '/product/:id',
          component: () => import('@/views/product/ProductDetail.vue')
        },
        {
          path: '/product/new',
          component: () => import('@/views/product/ProductNew.vue')
        },
        {
          path: '/product/posted',
          component: () => import('@/views/product/ProductPosted.vue')
        },
        {
          path: '/product/:id/modify',
          component: () => import('@/views/product/ProductModify.vue')
        },
        {
          path: '/product/star',
          component: () => import('@/views/product/ProductStar.vue')
        },
        {
          path: '/product/cart',
          component: () => import('@/views/product/ProductCart.vue')
        },
        {
          path: '/order/consumer',
          component: () => import('@/views/order/Consumer.vue')
        },
        {
          path: '/order/seller',
          component: () => import('@/views/order/Seller.vue')
        }
      ]
    },
    {
      path: '/admin',
      component: () => import('@/views/admin/AdminLayoutContainer.vue'),
      redirect: '/admin/home',
      children: [
        {
          path: '/admin/home',
          component: () => import('@/views/admin/AdminHomePage.vue')
        },
        {
          path: '/admin/user/new',
          component: () => import('@/views/admin/user/UserNew.vue')
        },
        {
          path: '/admin/user/list',
          component: () => import('@/views/admin/user/UserList.vue')
        }
      ]
    }
  ]
})

router.beforeEach(async (to, from) => {
  // 如果没有token, 且访问的是非登录页，拦截到登录页，其他情况正常放行
  const userStore = useUserStore()
  if (!userStore.token && to.path !== '/login') return '/login'
  // // 如果当前商品不是用户创建的, 用户不能访问该商品的修改信息页
  // const productStore = useProductStore()
  // if (!productStore.postProductList && )
  if (to.path === '/admin/home') {
    const res = await permissionJudgeAdminService()
    console.log(res.data.data.ifAdmin)
    if (res.data.data.ifAdmin === false) {
      ElMessage.error('您没有管理员权限')
      return '/home'
    }
  }
})

export default router
