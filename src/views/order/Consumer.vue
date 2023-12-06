<script setup>
import { onMounted, ref } from 'vue'
import { useOrderStore } from '@/stores'
import { ElMessageBox } from 'element-plus'
import { orderChangeStateService } from '@/api/order'

const orderStore = useOrderStore()
onMounted(() => {
  orderStore.getOrderConsumer()
})
const changeState = async (id, state) => {
  await ElMessageBox.confirm('你确认要收货么', '温馨提示', {
    type: 'warning',
    confirmButtonText: '确认',
    cancelButtonText: '取消'
  })
  await orderChangeStateService({ id, state })
  orderStore.getOrderConsumer()
}

const showType = ref('已完成')
</script>
<template>
  <!-- {{ orderStore.orderConsumerList }}
  <hr />
  {{
    orderStore.orderConsumerList.filter(
      (element) => element.status === 'Completed'
    )
  }} -->
  <div>
    <el-radio-group v-model="showType" size="large">
      <el-radio-button label="已完成" />
      <el-radio-button label="未完成" />
    </el-radio-group>
  </div>
  <template v-if="showType === '已完成'">
    <div
      v-if="
        orderStore.orderConsumerList.filter(
          (element) => element.status === 'Completed'
        ).length == 0
      "
    >
      您没有已完成的订单
    </div>
    <el-descriptions
      v-else
      :column="3"
      v-for="order in orderStore.orderConsumerList.filter(
        (element) => element.status === 'Completed'
      )"
      :key="order"
      :title="`您于${order.createdTime}创建的订单`"
      border
    >
      <el-descriptions-item label="商品名" label-align="right" align="center">
        {{ order.product.productName }}
      </el-descriptions-item>

      <el-descriptions-item label="商品单价" label-align="right" align="center">
        {{ order.product.price }}
      </el-descriptions-item>
      <el-descriptions-item label="购买数量" label-align="right" align="center">
        {{ order.number }}
      </el-descriptions-item>
      <el-descriptions-item label="应付金额" label-align="right" align="center">
        {{ order.number * order.product.price }}
      </el-descriptions-item>
      <el-descriptions-item label="订单状态" label-align="right" align="center">
        {{ order.status }}
      </el-descriptions-item>

      <el-descriptions-item
        label="收货人姓名"
        label-align="right"
        align="center"
      >
        {{ order.buyerInfo.name }}
      </el-descriptions-item>
      <el-descriptions-item
        label="收货人电话"
        label-align="right"
        align="center"
      >
        {{ order.buyerInfo.phone }}
      </el-descriptions-item>
      <el-descriptions-item
        label="收货人地址"
        label-align="right"
        align="center"
      >
        {{ order.buyerInfo.place }}
      </el-descriptions-item>
    </el-descriptions>
  </template>
  <template v-else-if="showType === '未完成'">
    <p>若未发货,请等待卖家与您提供的手机号联系并发货</p>
    <el-descriptions
      :column="3"
      v-for="order in orderStore.orderConsumerList.filter(
        (element) => element.status !== 'Completed'
      )"
      :key="order"
      :title="`您于${order.createdTime}创建的订单`"
      border
    >
      <template #extra v-if="order.status === 'InTransit'">
        <el-button type="danger" @click="changeState(order.id, 'Completed')"
          >设为已收货</el-button
        >
      </template>

      <el-descriptions-item label="商品名" label-align="right" align="center">
        {{ order.product.productName }}
      </el-descriptions-item>

      <el-descriptions-item label="商品单价" label-align="right" align="center">
        {{ order.product.price }}
      </el-descriptions-item>
      <el-descriptions-item label="购买数量" label-align="right" align="center">
        {{ order.number }}
      </el-descriptions-item>
      <el-descriptions-item label="应付金额" label-align="right" align="center">
        {{ order.number * order.product.price }}
      </el-descriptions-item>
      <el-descriptions-item label="订单状态" label-align="right" align="center">
        {{ order.status }}
      </el-descriptions-item>

      <el-descriptions-item
        label="收货人姓名"
        label-align="right"
        align="center"
      >
        {{ order.buyerInfo.name }}
      </el-descriptions-item>
      <el-descriptions-item
        label="收货人电话"
        label-align="right"
        align="center"
      >
        {{ order.buyerInfo.phone }}
      </el-descriptions-item>
      <el-descriptions-item
        label="收货人地址"
        label-align="right"
        align="center"
      >
        {{ order.buyerInfo.place }}
      </el-descriptions-item>
    </el-descriptions>
  </template>
</template>

<style scoped></style>
