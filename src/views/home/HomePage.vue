<script setup>
import { onMounted } from 'vue'
import { useProductStore, useStatisticStore } from '@/stores'

// 组件
import HomeStatistic from '@/components/statistic/HomeStatistic.vue'
import ProductCard from '@/components/product/ProductCard.vue'
const productStore = useProductStore()
const statisticStore = useStatisticStore()
onMounted(() => {
  productStore.getProducts()
  statisticStore.getActiveUserCount()
  statisticStore.getProductCount()
  statisticStore.getCommentCount()
  statisticStore.getActiveOrderCount()
})
</script>
<template>
  <div class="common-layout">
    <el-container>
      <HomeStatistic
        :activeUser="statisticStore.activeUserCount"
        :weeklyTrans="statisticStore.activeOrderCount"
        :productNum="statisticStore.productCount"
        :commentCount="statisticStore.commentCount"
      ></HomeStatistic>
      <br />
      <el-header>猜你喜欢</el-header>
      <el-main style="margin-left: 1%; margin-right: 1%">
        <el-row :gutter="20" class="el-row">
          <el-col
            :span="6"
            v-for="product in productStore.productList"
            :key="product.id"
          >
            <ProductCard
              :product="product"
              style="margin-top: 15px"
            ></ProductCard>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>
<style lang="scss" scoped>
.el-row {
  margin-bottom: 50px;
}
</style>
