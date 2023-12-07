<script setup>
import { ref, onMounted } from 'vue'
import { useMessageStore } from '@/stores'
const messageStore = useMessageStore()
onMounted(() => {
  messageStore.getMessageList()
})
const activeNames = ref(['1'])
</script>
<template>
  <el-row>
    <el-col :span="1"></el-col>
    <el-col :span="22">
      <div v-if="messageStore.messageList.length === 0">
        <p style="text-indent: 2em">您没有收到消息</p>
      </div>
      <div v-else>
        <el-collapse v-model="activeNames" @change="handleChange">
          <el-collapse-item
            v-for="(message, item, i) in messageStore.messageList"
            :key="message"
            :title="message.sender.userName + '给您发送的消息'"
            :name="i"
            style="text-indent: 2em"
            >{{ message.content }}
          </el-collapse-item>
        </el-collapse>
      </div>
    </el-col>
    <el-col :span="1"></el-col>
  </el-row>
</template>
<style scoped></style>
