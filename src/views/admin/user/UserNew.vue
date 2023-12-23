<script setup>
import { ref } from 'vue'
import { userRegisterService, userUploadExcelService } from '@/api/user.js'
import { ElMessage } from 'element-plus'
const form = ref()
const formModel = ref({
  userName: '',
  email: '',
  password: ''
})
const rules = {
  userName: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 5, max: 10, message: '用户名必须是 5-10位 的字符', trigger: 'blur' }
  ],
  email: [
    {
      pattern: /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$/,
      message: '请输入正确格式的邮箱',
      trigger: 'blur'
    }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    {
      pattern: /^\S{6,15}$/,
      message: '密码必须是 6-15位 的非空字符',
      trigger: 'blur'
    }
  ]
}
const addUser = async () => {
  // 成功之前，先进行校验，校验成功 → 请求，校验失败 → 自动提示
  await form.value.validate()
  await userRegisterService(formModel.value)
  ElMessage.success('添加用户成功')
}
let file = new ref()
const upload = (event) => {
  file = event.target.files[0]
}
const submit = async () => {
  let formData = new FormData()
  formData.append('file', file)
  const res = await userUploadExcelService(formData)
  if (res.data.code === 200) {
    ElMessage.success('批量添加用户成功')
  }
  // 失败提示由响应拦截器去做
}
</script>
<template>
  <div>
    <el-form
      :model="formModel"
      :rules="rules"
      ref="form"
      size="large"
      autocomplete="off"
    >
      <el-form-item>
        <h1>新增单个用户</h1>
      </el-form-item>
      <el-form-item prop="userName">
        <el-input
          v-model="formModel.userName"
          :prefix-icon="User"
          placeholder="请输入用户名"
        ></el-input>
      </el-form-item>
      <el-form-item prop="email">
        <el-input
          v-model="formModel.email"
          :prefix-icon="Message"
          placeholder="请输入邮箱"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          v-model="formModel.password"
          :prefix-icon="Lock"
          type="password"
          placeholder="请输入密码"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button
          @click="addUser"
          class="button"
          type="primary"
          auto-insert-space
        >
          添加用户
        </el-button>
      </el-form-item>
    </el-form>
  </div>
  <div>
    <h1>批量导入用户</h1>
    <em>仅支持指定格式的excel文件</em>
    <br />
    <br />
    <input type="file" @change="upload($event)" />
    <button @click="submit($event)">确认上传</button>
  </div>
</template>
