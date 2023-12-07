<script setup>
import { onMounted } from 'vue'
import { useProductStore } from '@/stores'
import { ElMessage } from 'element-plus'
import router from '@/router'
import AskPromotionButton from '@/components/promotion/AskPromotionButton.vue'
// 组件
// import PostStatistic from '@/components/statistic/PostStatistic.vue'
const productStore = useProductStore()
onMounted(() => {
  productStore.getPostedProducts()
})
const jump2Details = (key) => {
  const ownJudge = productStore.postProductList.some(
    (product) => product.productId === key
  )
  // TODO 把商品所属检测搞成全局/后端检测
  if (ownJudge) {
    router.push(`/product/${key}/modify`)
  } else {
    ElMessage.error('你没有该商品的修改权限')
  }
}
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
      v-for="product in productStore.postProductList"
      :key="product"
    >
      <el-card
        :body-style="{ padding: '0px' }"
        style="margin-top: 15px"
        @click.stop="jump2Details(product.productId)"
        class="hover-zoom"
      >
        <el-image
          :src="product.productPic[0]"
          style="width: 100%; height: 200px"
        />
        <el-row style="padding-left: 14px"
          ><h1>{{ product.productName }}</h1></el-row
        >
        <el-row style="padding-left: 14px">
          <div class="price">
            <span class="price1">¥</span
            ><span class="price2">{{ product.price }}</span>
          </div>
        </el-row>
        <el-row style="padding-left: 14px; padding-top: 5px">
          <el-col :span="8"
            ><el-button
              type="primary"
              @click.stop="jump2Details(product.productId)"
              >详情页</el-button
            ></el-col
          >
          <el-col :span="8"
            ><AskPromotionButton
              :productId="product.productId"
            ></AskPromotionButton>
          </el-col>
          <el-col :span="8"></el-col>
        </el-row>

        <el-row class="time">创建于{{ product.createdTime }}</el-row>
      </el-card>
    </el-col>
  </el-row>
</template>

<style scoped>
.time {
  text-align: center;
  color: gray;
  font-size: smaller;
  padding: 14px;
}
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
.price {
  display: flex;
  justify-content: flex-end;
}
.price1 {
  color: rgb(255, 80, 0);
  font-size: medium;
}
.price2 {
  color: rgb(255, 80, 0);
  font-size: large;
}
</style>
