<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { messageNewService } from '@/api/message'
defineOptions({
  name: 'MessageButton'
})
const props = defineProps({
  userName: String
})
const dialogVisible = ref(false)
const callMessageDialog = () => {
  dialogVisible.value = true
}
const submitMessage = async () => {
  const userName = props.userName
  const content = textarea.value
  await messageNewService({ userName, content })
  ElMessage.success('成功发送私信')
  dialogVisible.value = false
}
const textarea = ref('')
</script>
<template>
  <el-button @click="callMessageDialog">私信Ta</el-button>
  <el-dialog
    v-model="dialogVisible"
    :title="'给' + props.userName + '的私信'"
    width="40%"
  >
    <el-input
      v-model="textarea"
      :rows="3"
      type="textarea"
      placeholder="Please input"
    />
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="submitMessage()"> 发送 </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<style scoped></style>
