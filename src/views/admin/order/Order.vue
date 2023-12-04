<script setup>
import { onMounted } from 'vue'
import { useOrderStore } from '@/stores'
import { orderChangeStateService, orderDeleteOrderService } from '@/api/order'
const orderStore = useOrderStore()
onMounted(() => {
  orderStore.getOrderList()
})
const changeState = async (id, state) => {
  await orderChangeStateService({ id, state })
  orderStore.getOrderList()
}
const deleteOrder = async (id) => {
  await orderDeleteOrderService({ id })
  orderStore.getOrderList()
}
</script>
<template>
  <h1>All Orders</h1>
  <!-- {{ orderStore.orderList }} -->
  <el-descriptions
    :column="3"
    v-for="order in orderStore.orderList"
    :key="order"
    :title="`订单${order.id}`"
    border
  >
    <template #extra>
      <el-button type="danger" @click="deleteOrder(order.id)"
        >删除订单</el-button
      >
    </template>
    <el-descriptions-item
      label="订单创建时间"
      label-align="right"
      label-class-name="my-label"
      class-name="my-content"
      width="150px"
      >{{ order.createdTime }}</el-descriptions-item
    >
    <el-descriptions-item
      label="买家用户名"
      label-align="right"
      align="center"
      width="150px"
      >{{ order.buyer.userName }}</el-descriptions-item
    >
    <el-descriptions-item
      label="卖家用户名"
      label-align="right"
      align="center"
      width="150px"
      >{{ order.seller.userName }}</el-descriptions-item
    >
    <el-descriptions-item label="商品名" label-align="right" align="center">
      {{ order.product.productName }}
    </el-descriptions-item>
    <el-descriptions-item label="商品种类" label-align="right" align="center">
      {{ order.product.typeName }}
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
      label="收货信息"
      :span="3"
      label-align="right"
      align="center"
    >
    </el-descriptions-item>
    <el-descriptions-item label="收货人姓名" label-align="right" align="center">
      {{ order.buyerInfo.name }}
    </el-descriptions-item>
    <el-descriptions-item label="收货人电话" label-align="right" align="center">
      {{ order.buyerInfo.phone }}
    </el-descriptions-item>
    <el-descriptions-item label="收货人地址" label-align="right" align="center">
      {{ order.buyerInfo.place }}
    </el-descriptions-item>
    <el-descriptions-item
      label="修改订单状态"
      label-align="right"
      align="center"
    >
      <el-button type="primary" @click="changeState(order.id, 'ToBeShipped')"
        >修改为待发货</el-button
      >
      <el-button type="primary" @click="changeState(order.id, 'InTransit')"
        >修改为运输中</el-button
      >
      <el-button type="primary" @click="changeState(order.id, 'Completed')"
        >修改为已完成</el-button
      >
    </el-descriptions-item>
  </el-descriptions>
</template>
