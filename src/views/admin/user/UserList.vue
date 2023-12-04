<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores'
import { userDeleteUserService } from '@/api/user.js'
import { ElMessage } from 'element-plus'
import default_avatar from '@/assets/user/default.png'
const userStore = useUserStore()
onMounted(() => {
  userStore.getUserList()
})

const handleDelete = async (userName) => {
  await userDeleteUserService({ userName })
  ElMessage.success('删除成功')
  userStore.getUserList()
}
</script>
<template>
  <!-- 这是用户列表 {{ userStore.userList }} -->
  <el-table :data="userStore.userList" style="width: 100%">
    <el-table-column prop="avatar" label="Avatar" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <el-avatar :src="scope.row.avatar || default_avatar" />
        </div>
      </template>
    </el-table-column>
    <el-table-column prop="userName" label="Name" width="180" />
    <el-table-column prop="email" label="Email" width="180" />
    <el-table-column prop="registerTime" label="register time" width="180" />
    <el-table-column prop="userName" label="Operation" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <el-button
            size="small"
            type="danger"
            @click="handleDelete(scope.row.userName)"
            >Delete</el-button
          >
        </div>
      </template>
    </el-table-column>
  </el-table>
</template>
