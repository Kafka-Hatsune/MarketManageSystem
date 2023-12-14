<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores'
import { userDeleteUserService } from '@/api/user.js'
import { ElMessage } from 'element-plus'
import default_avatar from '@/assets/user/default.png'
const userStore = useUserStore()
onMounted(() => {
  userStore.getAdminList()
})

const handleDelete = async (userName) => {
  const res = await userDeleteUserService({ userName })
  if (res.data.code === 200) {
    ElMessage.success('删除成功')
  }
  userStore.getAdminList()
}
</script>
<template>
  <el-table :data="userStore.adminList" style="width: 100%">
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
    <el-table-column
      prop="userName"
      label="Operation"
      width="240"
      style="align-items: center"
    >
      <template #default="scope">
        <el-row :gutter="2">
          <el-col :span="12">
            <el-button
              size="small"
              type="danger"
              @click="handleDelete(scope.row.userName)"
              >删除管理员</el-button
            ></el-col
          >
        </el-row>
      </template>
    </el-table-column>
  </el-table>
</template>
