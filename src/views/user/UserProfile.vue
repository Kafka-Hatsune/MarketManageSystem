<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores'
import { userUpdateInfoService } from '@/api/user'
import { ElMessage } from 'element-plus'
// 组件
import AvatarLoader from '../../components/user/AvatarLoader.vue'
import PageContainer from '@/components/PageContainer.vue'
import RecInforDisplayer from '@/components/user/RecInforDisplayer.vue'

const formRef = ref()
const userStore = useUserStore()
onMounted(() => {
  userStore.getCurRecInfor()
  userStore.getAllRecInfor()
})

// 是在使用仓库中数据的初始值 (无需响应式) 解构无问题
const {
  user: { email, id, userName, avatar },
  getUser
} = useUserStore()

const form = ref({
  id,
  userName,
  email,
  avatar
})

const rules = ref({
  email: [
    { required: true, message: '请输入用户邮箱', trigger: 'blur' },
    {
      type: 'email',
      message: '请输入正确的邮箱格式',
      trigger: ['blur', 'change']
    }
  ]
})

const submitForm = async () => {
  // 等待校验结果
  await formRef.value.validate()
  // 提交修改
  await userUpdateInfoService(form.value)
  // 通知 user 模块，进行数据的更新
  getUser()
  // 提示用户
  ElMessage.success('修改成功')
}
</script>
<template>
  <page-container title="基本资料">
    <br />
    <div class="common-layout">
      <el-container>
        <el-aside width="350px">
          <!-- <h3 class="center">用户头像</h3> -->
          <el-row>
            <el-col :span="8"></el-col>
            <el-col :span="8">
              <div class="center">用户头像</div>
            </el-col>
            <el-col :span="8"></el-col>
          </el-row>
          <br />
          <el-row>
            <el-col :span="3"></el-col>
            <el-col :span="18"><AvatarLoader></AvatarLoader></el-col>
            <el-col :span="3"></el-col>
          </el-row>
        </el-aside>
        <el-main>
          <!-- 表单部分 -->
          <el-form
            ref="formRef"
            :model="form"
            :rules="rules"
            label-width="100px"
          >
            <el-form-item label="登录用户名">
              <el-input v-model="form.userName" disabled></el-input>
            </el-form-item>
            <el-form-item label="用户邮箱" prop="email">
              <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm">提交修改</el-button>
            </el-form-item>
          </el-form>
          <RecInforDisplayer></RecInforDisplayer>
        </el-main>
      </el-container>
    </div>
  </page-container>
</template>
<style scoped>
.center {
  text-align: center;
}
.centerBlock {
  margin: 0 auto;
}
.out-box {
  display: flex;

  border: 1px solid #000;
}
.inner-box {
  margin-left: 10px;
  margin-right: 10px;
  /* margin: auto; */
}
</style>
