<script setup>
import { userUpdateAvatarService } from '@/api/user'
import { ref } from 'vue'
import { useUserStore } from '@/stores'
import { ElMessage } from 'element-plus'

const userStore = useUserStore()
let file = new ref()
const imgUrl = new ref()
const upload = (event) => {
  file = event.target.files[0]
  const reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onload = () => {
    imgUrl.value = reader.result
  }
}
const submit = async () => {
  let formData = new FormData()
  formData.append('avatar', file)
  await userUpdateAvatarService(formData)
  // userStore 重新渲染
  await userStore.getUser()
  // 提示用户
  ElMessage.success('头像更新成功')
}
</script>
<template>
  <el-avatar v-if="imgUrl" :src="imgUrl" class="avatar" />
  <el-avatar v-else :src="userStore.user.avatar" class="avatar" />
  <br />
  <el-row>
    <el-col><input type="file" @change="upload($event)" /></el-col>
  </el-row>
  <el-row>
    <button @click="submit($event)">确认上传</button>
  </el-row>
</template>

<style scoped>
.avatar {
  width: 250px;
  height: 250px;
  display: block;
}
</style>
