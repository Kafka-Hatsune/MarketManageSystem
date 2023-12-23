<script setup>
import {
  UserFilled,
  User,
  Crop,
  EditPen,
  SwitchButton,
  CaretBottom,
  HomeFilled,
  Plus,
  List,
  Monitor
} from '@element-plus/icons-vue'
import { ElMessageBox } from 'element-plus'
import avatar from '@/assets/user/default.png'
import { useUserStore } from '@/stores'
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'

// 组件
import CurrentTime from '@/components/timer/Clock.vue'

const userStore = useUserStore()
const router = useRouter()
const currentTime = computed(() => new Date().getHours())
const greeting = computed(() => {
  if (currentTime.value >= 0 && currentTime.value < 12) {
    return '早上好'
  } else if (currentTime.value >= 12 && currentTime.value < 18) {
    return '下午好'
  } else {
    return '晚上好'
  }
})
onMounted(() => {
  userStore.getUser()
})

const handleCommand = async (key) => {
  if (key === 'logout') {
    // 退出操作
    await ElMessageBox.confirm('你确认要进行退出么', '温馨提示', {
      type: 'warning',
      confirmButtonText: '确认',
      cancelButtonText: '取消'
    })

    // 清除本地的数据 (token + user信息)
    userStore.removeToken()
    userStore.setUser({})
    router.push('/login')
  } else {
    // 跳转操作
    router.push(`/user/${key}`)
  }
}
</script>

<template>
  <el-container class="layout-container">
    <!-- 侧边栏 -->
    <el-aside width="200px">
      <!-- <div class="el-aside__logo"></div> -->
      <!-- el-menu 整个菜单组件 
        :default-active="$route.path" 配置默认高亮的菜单项
        router router选项开启，el-menu-item 的 index 就是点击跳转的路径 -->
      <el-menu
        active-text-color="#ffd04b"
        background-color="#232323"
        :default-active="$route.path"
        text-color="#fff"
        router
      >
        <!-- el-menu-item 菜单项
          index="/article/channel" 配置的是访问的跳转路径，配合default-active的值，实现高亮 -->
        <el-menu-item index="/admin/home">
          <el-icon><HomeFilled /></el-icon>
          <span>管理员主页</span>
        </el-menu-item>

        <el-sub-menu index="/admin/user">
          <!-- 多级菜单的标题 - 具名插槽 title -->
          <template #title>
            <el-icon><UserFilled /></el-icon>
            <span>用户管理</span>
          </template>

          <!-- 展开的内容 - 默认插槽 -->
          <el-menu-item index="/admin/user/new">
            <el-icon><Plus /></el-icon>
            <span>新增用户</span>
          </el-menu-item>
          <el-menu-item index="/admin/user/list">
            <el-icon><List /></el-icon>
            <span>用户列表</span>
          </el-menu-item>
          <el-menu-item index="/admin/admin/list">
            <el-icon><Monitor /></el-icon>
            <span>管理员列表</span>
          </el-menu-item>
        </el-sub-menu>

        <el-menu-item index="/admin/order">
          <el-icon><List /></el-icon>
          <span>订单管理</span>
        </el-menu-item>
        <el-menu-item index="/home">
          <el-icon><SwitchButton /></el-icon>
          <span>退出管理员页面</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <!-- 上边栏 -->
    <el-container>
      <!-- header -->
      <el-header>
        <el-col :span="8"></el-col>
        <el-col :span="8"></el-col>
        <el-col :span="4">
          <div><CurrentTime></CurrentTime></div>
        </el-col>
        <el-col :span="3">
          {{ userStore.user.userName }} : {{ greeting }}
        </el-col>
        <el-col :span="2">
          <el-dropdown placement="bottom-end" @command="handleCommand">
            <!-- 展示给用户，默认看到的 -->
            <span class="el-dropdown__box">
              <el-avatar :src="userStore.user.avatar || avatar" />
              <el-icon><CaretBottom /></el-icon>
            </span>

            <!-- 折叠的下拉部分 -->
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="profile" :icon="User"
                  >基本资料</el-dropdown-item
                >
                <el-dropdown-item command="avatar" :icon="Crop"
                  >更换头像</el-dropdown-item
                >
                <el-dropdown-item command="password" :icon="EditPen"
                  >重置密码</el-dropdown-item
                >
                <el-dropdown-item command="logout" :icon="SwitchButton"
                  >退出登录</el-dropdown-item
                >
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </el-col>
      </el-header>
      <!-- 主要区域容器 -->
      <el-main>
        <router-view></router-view>
      </el-main>
      <!-- footer -->
      <el-footer>It's MyGO!!©2023</el-footer>
    </el-container>
  </el-container>
</template>

<style lang="scss" scoped>
.layout-container {
  height: 100vh;
  .el-aside {
    background-color: #232323;
    &__logo {
      height: 120px;
      background: url('@/assets/logo.png') no-repeat center / 120px auto;
    }
    .el-menu {
      border-right: none;
    }
  }
  .el-header {
    background-color: #fff;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    .el-dropdown__box {
      display: flex;
      align-items: center;
      .el-icon {
        color: #999;
        margin-left: 10px;
      }

      &:active,
      &:focus {
        outline: none;
      }
    }
  }
  .el-footer {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    color: #666;
  }
}
</style>
