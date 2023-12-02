<script setup>
import { onMounted } from 'vue'
import { useOrderStore } from '@/stores'
import { ElMessage } from 'element-plus'
import router from '@/router'

// 组件
// import PostStatistic from '@/components/statistic/PostStatistic.vue'
const orderStore = useOrderStore()
onMounted(() => {
  orderStore.getOrderSeller()
})
console.log('--------------------------------')
console.log('<orderSeller>')
console.log(orderStore.orderSellerList)
console.log('--------------------------------')
</script>
<template>
  <!-- {{ productStore.postProductList }} -->
  <hr />
  <el-row :gutter="20">
    <el-col
      :span="4"
      v-for="order in orderStore.orderSellerList"
      :key="order"
    >
      <el-card
        :body-style="{ padding: '0px' }"
        style="margin-top: 15px"
        @click.stop="jump2Details(props.product.productId)"
        class="hover-zoom"
      >
        <el-image
          :src="order.product.productPic[0]"
          style="width: 200px; height: 200px"
        />
        <div style="padding: 14px">
          <span>{{ order.product.ProductName }}</span>
          <div class="price">
            <span class="price1"></span
            ><span class="price2">从 {{ order.seller.userName }} 购买 {{ order.number }} 件</span>
          </div>
          <div class="price">
            <span class="price1">实付 ¥</span
            ><span class="price2">{{ order.product.price*order.number }}</span>
          </div>
          <div class="bottom">
            <time class="time">{{ order.product.createdTime }}</time>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>

  <!-- {{ productStore.postProductList }} -->
</template>

<style scoped>
el-col {
  text-align: center;
}
.hover-zoom {
  width: auto;
  height: auto;
}
.hover-zoom:hover {
  transform: scale(1.05);
  transition: all 0.3s ease-in-out;
}
.center {
  margin-left: auto;
  margin-right: auto;
}
</style>
