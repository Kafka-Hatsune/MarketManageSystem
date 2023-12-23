<script setup>
import {
  Promotion,
  UserFilled,
  User,
  Crop,
  EditPen,
  SwitchButton,
  CaretBottom,
  Goods,
  ShoppingTrolley,
  StarFilled,
  UploadFilled,
  HomeFilled,
  WalletFilled,
  Wallet,
  Calendar,
  BellFilled,
  Bell
} from '@element-plus/icons-vue'
import { ElMessageBox } from 'element-plus'
import avatar from '@/assets/user/default.png'
import { useUserStore, useMessageStore } from '@/stores'
import { onMounted, computed, ref } from 'vue'
import { useRouter } from 'vue-router'

// 组件
import CurrentTime from '@/components/timer/Clock.vue'

const userStore = useUserStore()
const messageStore = useMessageStore()
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
  messageStore.queryIfHasUnreadMessage()
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

const askPermissionForAdmin = async () => {
  // 放在路由守卫中判断权限
  router.push('/admin/home')
}
const activeNames = ref(['1'])
const drawer = ref(false)
const callDrawer = () => {
  messageStore.getUnreadMessageList()
  drawer.value = true
}
const handleClose = () => {
  messageStore.queryIfHasUnreadMessage()
  drawer.value = false
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
        background-color="#2a5b87"
        :default-active="$route.path"
        text-color="#fff"
        router
      >
        <!-- el-menu-item 菜单项
          index="/article/channel" 配置的是访问的跳转路径，配合default-active的值，实现高亮 -->
        <el-menu-item index="/home">
          <el-icon>
            <HomeFilled />
          </el-icon>
          <span>主页</span>
        </el-menu-item>

        <el-sub-menu index="/product">
          <!-- 多级菜单的标题 - 具名插槽 title -->
          <template #title>
            <el-icon>
              <Goods />
            </el-icon>
            <span>商品管理</span>
          </template>

          <!-- 展开的内容 - 默认插槽 -->
          <el-menu-item index="/product/new">
            <el-icon>
              <Promotion />
            </el-icon>
            <span>发布新商品</span>
          </el-menu-item>
          <el-menu-item index="/product/posted">
            <el-icon>
              <UploadFilled />
            </el-icon>
            <span>我的已发布商品</span>
          </el-menu-item>
          <el-menu-item index="/product/star">
            <el-icon>
              <StarFilled />
            </el-icon>
            <span>收藏夹</span>
          </el-menu-item>
          <el-menu-item index="/product/cart">
            <el-icon>
              <ShoppingTrolley />
            </el-icon>
            <span>购物车</span>
          </el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="/order">
          <!-- 多级菜单的标题 - 具名插槽 title -->
          <template #title>
            <el-icon>
              <Calendar />
            </el-icon>
            <span>订单管理</span>
          </template>

          <!-- 展开的内容 - 默认插槽 -->
          <el-menu-item index="/order/consumer">
            <el-icon>
              <Wallet />
            </el-icon>
            <span>我的购买</span>
          </el-menu-item>
          <el-menu-item index="/order/seller">
            <el-icon>
              <WalletFilled />
            </el-icon>
            <span>我的卖出</span>
          </el-menu-item>
        </el-sub-menu>

        <el-menu-item index="/user/profile">
          <el-icon>
            <UserFilled />
          </el-icon>
          <span>个人中心</span>
        </el-menu-item>
        <el-menu-item @click="askPermissionForAdmin">
          <el-icon>
            <UserFilled />
          </el-icon>
          <span>管理员页面</span>
        </el-menu-item>
        <el-menu-item @click="handleCommand('logout')">
          <el-icon>
            <SwitchButton />
          </el-icon>
          <span>退出登陆</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <!-- 上边栏 -->
    <el-container>
      <!-- header -->
      <el-header>
        <el-col :span="14"></el-col>
        <el-col :span="4">
          <div>
            <CurrentTime></CurrentTime>
          </div>
        </el-col>
        <el-col :span="3">
          {{ userStore.user.userName }} : {{ greeting }}
        </el-col>
        <el-col :span="1">
          <el-icon
            v-if="messageStore.ifHas"
            @click="callDrawer()"
            class="message-red"
          >
            <BellFilled
          /></el-icon>
          <el-icon v-else @click="callDrawer()" class="message"
            ><Bell
          /></el-icon>
        </el-col>
        <el-col :span="2">
          <el-dropdown placement="bottom-end" @command="handleCommand">
            <!-- 展示给用户，默认看到的 -->
            <span class="el-dropdown__box">
              <el-avatar :src="userStore.user.avatar || avatar" />
              <el-icon>
                <CaretBottom />
              </el-icon>
            </span>

            <!-- 折叠的下拉部分 -->
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="profile" :icon="User"
                  >基本资料</el-dropdown-item
                >
                <el-dropdown-item command="message" :icon="Crop"
                  >消息中心</el-dropdown-item
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

  <!-- 抽屉 -->
  <el-drawer v-model="drawer" title="未读消息列表" :before-close="handleClose">
    <div v-if="messageStore.unreadMessageList.length === 0">您没有未读消息</div>
    <div v-else>
      <el-collapse v-model="activeNames" @change="handleChange">
        <el-collapse-item
          v-for="(message, item, i) in messageStore.unreadMessageList"
          :key="message"
          :title="message.sender.userName + '给您发送的消息'"
          :name="i"
          >{{ message.content }}
        </el-collapse-item>
      </el-collapse>
    </div>
  </el-drawer>
</template>

<style lang="scss" scoped>
.message {
  cursor: pointer;
}
.message-red {
  cursor: pointer;
  color: red;
}
.layout-container {
  height: 100vh;

  .el-aside {
    // background-color: #d8aeb0;
    background-color: #2a5b87;

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
