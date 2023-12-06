<script setup>
defineOptions({
  name: 'RecInforDisplayer'
})
import { useUserStore } from '@/stores'
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
const userStore = useUserStore()
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

  await userCreateRecInfoService(form.value)
  await userStore.getCurRecInfor()
  await userStore.getAllRecInfor()
  // 提示用户
  ElMessage.success('新建成功')
}
// 设置默认地址
const setDefaultRecInfor = async (id) => {
  await userSetDefaultRecInfoService({ id })
  await userStore.getCurRecInfor()
  await userStore.getAllRecInfor()
}
</script>
<template>
  <h2>用户收货信息</h2>
  <el-button @click="dialogFormVisible = true">新建收货信息</el-button>
  <div v-if="userStore.recInforList === null">当前没有收货信息,去新建</div>
  <hr />
  <div v-if="userStore.curRecInfor">
    <el-descriptions title="用户当前默认收货信息">
      <el-descriptions-item label="收货人姓名">{{
        userStore.curRecInfor.name
      }}</el-descriptions-item>
      <el-descriptions-item label="收货人电话">{{
        userStore.curRecInfor.phone
      }}</el-descriptions-item>
      <el-descriptions-item label="收货地址">
        {{ userStore.curRecInfor.place }}</el-descriptions-item
      >
    </el-descriptions>
  </div>
  <div height="400px" v-else>当前没有设置默认收货信息,去设置</div>
  <h2>您的其他收货地址</h2>
  <!-- 存在curRecInfor时的行为 -->
  <div v-if="userStore.curRecInfor">
    <el-tabs tab-position="left" style="height: 200px" class="demo-tabs">
      <el-tab-pane
        v-for="infor in userStore.recInforList.filter(
          (item) => item.id !== userStore.curRecInfor.id
        )"
        :key="infor"
        label="收货地址"
        ><el-descriptions title="">
          <el-descriptions-item label="收货人姓名">{{
            infor.name
          }}</el-descriptions-item>
          <el-descriptions-item label="收货人电话">{{
            infor.phone
          }}</el-descriptions-item>
          <el-descriptions-item label="收货地址">
            {{ infor.place }}</el-descriptions-item
          >
        </el-descriptions>
        <el-button class="rightButton" @click="setDefaultRecInfor(infor.id)">
          设置为默认地址
        </el-button>
      </el-tab-pane>
    </el-tabs>
  </div>
  <!-- 不存在recInfor的行为 -->
  <div v-else>
    <el-tabs tab-position="left" style="height: 200px" class="demo-tabs">
      <el-tab-pane
        v-for="infor in userStore.recInforList"
        :key="infor"
        label="收货地址"
        ><el-descriptions title="">
          <el-descriptions-item label="收货人姓名">{{
            infor.name
          }}</el-descriptions-item>
          <el-descriptions-item label="收货人电话">{{
            infor.phone
          }}</el-descriptions-item>
          <el-descriptions-item label="收货地址">
            {{ infor.place }}</el-descriptions-item
          >
        </el-descriptions>
        <el-button class="rightButton" @click="setDefaultRecInfor(infor.id)">
          设置为默认地址
        </el-button>
      </el-tab-pane>
    </el-tabs>
  </div>
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
