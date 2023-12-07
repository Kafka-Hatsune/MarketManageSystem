<script setup>
import { ElMessage } from 'element-plus'
import { promotionNewService } from '@/api/promotion'
defineOptions({
  name: 'AskPromotionButton'
})
const props = defineProps({
  productId: Number
})

const askPromotion = async () => {
  const productId = props.productId
  const res = await promotionNewService({ productId })
  if (res.data.code === 200) {
    ElMessage.success('成功提交申请,请等待审批')
  }
}
</script>
<template>
  <el-button type="warning" @click="askPromotion()">申请推广</el-button>
</template>
<style scoped></style>
