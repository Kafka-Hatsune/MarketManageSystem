<script setup>
defineOptions({
  name: 'CurrentTime'
})
import { ref, onMounted, onUnmounted } from 'vue'
// 格式化日期函数
const formatDate = (date) => {
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  const time = date.toLocaleTimeString()
  return `${year}-${month}-${day} ${time}`
}
const currentDate = ref(formatDate(new Date()))

const updateTime = () => {
  currentDate.value = formatDate(new Date())
}

// 在组件挂载时开始更新时间
onMounted(() => {
  setInterval(updateTime, 1000) // 每秒更新一次时间
})

// 在组件卸载时停止更新时间
onUnmounted(() => {
  clearInterval(updateTime)
})
</script>
<template>
  {{ currentDate }}
</template>
