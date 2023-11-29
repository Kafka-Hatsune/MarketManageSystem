import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores'
import { useProductStore } from '../stores/modules/product'

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
        }
      ]
    },
    {
      path: '/admin/',
      component: () => import('@/views/layout/AdminLayoutContainer.vue'),
      redirect: '/admin/home',
      children: [
        {
          path: '/admin/home',
          component: () => import('@/views/home/HomePage.vue')
        },
        {
          path: '/admin/user/profile',
          component: () => import('@/views/user/UserProfile.vue')
        },
        {
          path: '/admin/product/:id',
          component: () => import('@/views/product/ProductDetail.vue')
        },
        {
          path: '/admin/product/new',
          component: () => import('@/views/product/ProductNew.vue')
        },
        {
          path: '/admin/product/posted',
          component: () => import('@/views/product/ProductPosted.vue')
        },
        {
          path: '/admin/product/:id/modify',
          component: () => import('@/views/product/ProductModify.vue')
        },
        {
          path: '/admin/product/star',
          component: () => import('@/views/product/ProductStar.vue')
        },
        {
          path: '/admin/product/cart',
          component: () => import('@/views/product/ProductCart.vue')
        }
      ]
    }
  ]
})

router.beforeEach((to) => {
  // 如果没有token, 且访问的是非登录页，拦截到登录页，其他情况正常放行
  const userStore = useUserStore()
  if (!userStore.token && to.path !== '/login') return '/login'
  // // 如果当前商品不是用户创建的, 用户不能访问该商品的修改信息页
  // const productStore = useProductStore()
  // if (!productStore.postProductList && )
})

export default router
