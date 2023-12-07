<script setup>
import { onMounted, ref } from 'vue'
import { useProductStore, useStatisticStore, usePromotionStore } from '@/stores'
import { useRouter } from 'vue-router'
// 组件
import HomeStatistic from '@/components/statistic/HomeStatistic.vue'
import ProductCard from '@/components/product/ProductCard.vue'
const router = useRouter()
const productStore = useProductStore()
const statisticStore = useStatisticStore()
const promotionStore = usePromotionStore()
const promotionDialog = ref(false)
const ifShow = ref(true)
onMounted(async () => {
  productStore.getProducts()
  statisticStore.getActiveUserCount()
  statisticStore.getProductCount()
  statisticStore.getCommentCount()
  statisticStore.getActiveOrderCount()
  await promotionStore.getPromotionActiveList()
  if (promotionStore.ifShow && promotionStore.promotionActiveList.length > 0) {
    promotionDialog.value = true
  }
})
const jump2Details = (key) => {
  router.push(`/product/${key}`)
}
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

  <el-dialog v-model="promotionDialog" title="当前热销商品" width="40%">
    <div
      v-for="(product, item, index) in promotionStore.promotionActiveList"
      :key="product"
    >
      <el-row>
        <el-col :span="10"
          >当前爆款{{ index }}&nbsp;:&nbsp;{{ product.productName }}</el-col
        >
        <el-col :span="4">价格&nbsp;:&nbsp;{{ product.price }}元</el-col>
        <el-col :span="7"></el-col>
        <el-col :span="3"
          ><el-button @click="jump2Details(product.productId)" type="success"
            >去看看</el-button
          ></el-col
        >
        <el-col :span="2"></el-col>
      </el-row>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button
          @click="
            () => {
              promotionStore.ifShow = false
              promotionDialog = false
            }
          "
          >不再展示</el-button
        >
        <el-button @click="promotionDialog = false">关闭</el-button>
      </span>
    </template>
  </el-dialog>
</template>
<style lang="scss" scoped>
.el-row {
  margin-bottom: 50px;
}
</style>
