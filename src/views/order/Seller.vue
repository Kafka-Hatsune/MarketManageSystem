<script setup>
import { onMounted } from 'vue'
import { useOrderStore } from '@/stores'
import { useProductStore } from '@/stores'
import { ElMessage } from 'element-plus'
import router from '@/router'

// 组件
// import PostStatistic from '@/components/statistic/PostStatistic.vue'
const orderStore = useOrderStore()
const productStore = useProductStore()
onMounted(() => {
  productStore.getPostedProducts()
  orderStore.getOrderSeller()
})
const postProductList1 = productStore.postProductList
// productStore.postProductList.push({ productName: 111 })
console.log('--------------------------------')
console.log(postProductList1)
console.log(productStore.postProductList.at(0))
console.log('--------------------------------')
// const sales = productStore.postProductList.value.reduce((product, num) => {
//   console.log(product.value)
//   product.sale + num
// }, 0)
</script>
<template>
  <!-- {{ productStore.postProductList }} -->
  <!-- 统计已售出商品的数量 已售出商品的金额 在售商品的件数 与之完成订单的用户数 -->
  <el-row>
    <el-col :span="3"></el-col>
    <el-col :span="6">
      <el-statistic
        title="已售出商品量"
        :value="productStore.sales_quantity"
        class="center"
      />
    </el-col>
    <el-col :span="6">
      <el-statistic
        title="销售额"
        :value="productStore.sales_volume"
        style="margin: 0 auto"
      />
    </el-col>
    <el-col :span="6">
      <el-statistic
        title="在售商品数"
        :value="productStore.postProductList.length"
      />
    </el-col>
    <el-col :span="3"></el-col>
  </el-row>
  <hr />
  <el-row :gutter="20">
    <el-col
      :span="6"
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
            <span class="price1">¥</span
            ><span class="price2">{{ order.product.price }}</span>
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
