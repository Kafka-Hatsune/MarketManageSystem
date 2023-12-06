<script setup>
import { onMounted } from 'vue'
import { useOrderStore } from '@/stores'
import { useProductStore } from '@/stores'
import { ref } from 'vue'
import { orderChangeStateService } from '@/api/order'
// 组件
// import PostStatistic from '@/components/statistic/PostStatistic.vue'
const orderStore = useOrderStore()
const productStore = useProductStore()
onMounted(() => {
  productStore.getPostedProducts()
  orderStore.getOrderSeller()
})
const changeState = async (id, state) => {
  await orderChangeStateService({ id, state })
  orderStore.getOrderSeller()
}
// const completedOrder =
const showType = ref('已完成')
</script>
<template>
  <!-- {{ orderStore.orderSellerList }}
  <hr />
  {{
    orderStore.orderSellerList.filter(
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
        orderStore.orderSellerList.filter(
          (element) => element.status === 'Completed'
        ).length == 0
      "
    >
      您没有已完成的订单
    </div>
    <el-descriptions
      v-else
      :column="3"
      v-for="order in orderStore.orderSellerList.filter(
        (element) => element.status === 'Completed'
      )"
      :key="order"
      :title="`您于${order.createdTime}收到的订单`"
      border
    >
      <el-descriptions-item
        label="买家用户名"
        label-align="right"
        align="center"
        width="150px"
        >{{ order.buyer.userName }}</el-descriptions-item
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
    <el-descriptions
      :column="3"
      v-for="order in orderStore.orderSellerList.filter(
        (element) =>
          element.status === 'ToBeShipped' || element.status === 'InTransit'
      )"
      :key="order"
      :title="`您于${order.createdTime}收到的订单`"
      border
    >
      <template #extra v-if="order.status === 'ToBeShipped'">
        <el-button type="danger" @click="changeState(order.id, 'InTransit')"
          >设为已发货</el-button
        >
      </template>
      <el-descriptions-item
        label="买家用户名"
        label-align="right"
        align="center"
        width="150px"
        >{{ order.buyer.userName }}</el-descriptions-item
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
  <hr />
</template>

<style scoped></style>
