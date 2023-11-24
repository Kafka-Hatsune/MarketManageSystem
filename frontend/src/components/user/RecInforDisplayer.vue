<script setup>
defineOptions({
  name: 'RecInforDisplayer'
})
import { useUserStore } from '@/stores'
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
const userStore = useUserStore()
const userRecInfors = userStore.user.recInfors
const userCurInfor = userStore.user.recInfor
// 新建收货信息
import {
  userCreateRecInfoService,
  userSetDefaultRecInfoService
} from '@/api/user'
const dialogFormVisible = ref(false)
const recName = ref()
const phone = ref()
const place = ref()
const form = ref({
  recName,
  phone,
  place
})
// 提交表单行为
const submitNewRecInforForm = async () => {
  // 关闭对话框表单
  dialogFormVisible.value = false
  // 提交修改
  await userCreateRecInfoService(form.value)
  // 通知 user 模块，进行数据的更新
  userStore.getUser()
  // 提示用户
  ElMessage.success('新建成功')
}
// 设置默认地址
const setDefaultRecInfor = async (id) => {
  await userSetDefaultRecInfoService(id)
}
</script>
<template>
  <h2>用户收货信息</h2>
  <el-button @click="dialogFormVisible = true">新建收货信息</el-button>
  <template v-if="userRecInfors === null"> 当前没有收货信息,去新建 </template>
  <template v-else-if="userCurInfor === null">
    当前没有设置默认收货信息,去设置
  </template>
  <template v-else>
    <el-scrollbar height="400px">
      <div
        v-for="recInfor in userRecInfors"
        :key="recInfor"
        class="scrollbar-demo-item"
      >
        <div v-if="recInfor !== userCurInfo">
          <span>{{ recInfor.name }}</span>
          <span>{{ recInfor.phone }}</span>
          <br />
          {{ recInfor.place }}
        </div>
        <div v-else class="">
          <span>{{ recInfor.name }}</span>
          <span>{{ recInfor.phone }}</span>
          <br />
          {{ recInfor.place }}
        </div>
        <el-button
          v-if="recInfor !== userCurInfo"
          class="rightButton"
          @click="setDefaultRecInfor(recInfor.id)"
        >
          设置为默认地址
        </el-button>
      </div>
    </el-scrollbar>
  </template>
  <!-- 新建收货信息表单 -->
  <el-dialog v-model="dialogFormVisible" title="新建收货信息">
    <el-form :model="form">
      <el-form-item label="收货人姓名" :label-width="formLabelWidth">
        <el-input v-model="form.recName" autocomplete="off" />
      </el-form-item>
      <el-form-item label="收货人电话" :label-width="formLabelWidth">
        <el-input v-model="form.phone" placeholder />
      </el-form-item>
      <el-form-item label="收货人地址" :label-width="formLabelWidth">
        <el-input v-model="form.place" placeholder />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submitNewRecInforForm">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<style scoped>
.scrollbar-demo-item {
  display: flex;
  align-items: left;
  justify-content: left;
  height: 50px;
  margin: 10px;
  text-align: left;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
.rightButton {
  margin-left: auto;
  margin-right: 0;
}

.el-button--text {
  margin-right: 15px;
}
.el-select {
  width: 300px;
}
.el-input {
  width: 300px;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>
