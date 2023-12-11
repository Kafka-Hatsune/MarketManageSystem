<script setup>
import { onMounted, ref } from 'vue'
import { usePromotionStore, useProductStore } from '@/stores'
import { promotionUpdateService, promotionDeleteService } from '@/api/promotion'
import default_avatar from '@/assets/user/default.png'
const promotionStore = usePromotionStore()
const productStore = useProductStore()
onMounted(() => {
  promotionStore.getPromotionList()
})
const drawer = ref(false)
const callDrawer = (productId) => {
  productStore.getProduct(productId)
  drawer.value = true
}
const submitPermit = async (productId) => {
  console.log(productId)
  await promotionUpdateService({ productId })
  await promotionStore.getPromotionList()
}
const submitRefuse = async (productId) => {
  console.log(productId)
  await promotionDeleteService({ productId })
  await promotionStore.getPromotionList()
}
</script>
<template>
  <el-table :data="promotionStore.promotionList" style="width: 100%">
    <el-table-column label="Avatar" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <el-avatar :src="scope.row.applicant.avatar || default_avatar" />
        </div>
      </template>
    </el-table-column>
    <el-table-column prop="applicant.userName" label="申请用户名" width="180" />
    <el-table-column label="Product" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <el-button type="primary" @click="callDrawer(scope.row.productId)">
            商品详情</el-button
          >
        </div>
      </template>
    </el-table-column>
    <el-table-column label="Operation" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <el-button type="success" @click="submitPermit(scope.row.productId)"
            >接受</el-button
          >
          <el-button type="danger" @click="submitRefuse(scope.row.productId)"
            >拒绝</el-button
          >
        </div>
      </template>
    </el-table-column>
  </el-table>

  <!-- 抽屉 -->
  <el-drawer v-model="drawer" title="商品详情" :direction="rtl">
    <div>
      <el-carousel class="carousel">
        <el-carousel-item
          v-for="productPic in productStore.product.productPic"
          :key="productPic"
        >
          <img :src="productPic" class="imgcar" />
        </el-carousel-item>
      </el-carousel>
    </div>
    <br />
    <div>商品名: {{ productStore.product.productName }}</div>
    <br />
    <div>价格: {{ productStore.product.price }}元</div>
    <br />
    <div>商品种类: {{ productStore.product.typeName }}</div>
    <br />
    <div>商品描述: {{ productStore.product.description }}</div>
    <br />
    <div>剩余库存: {{ productStore.product.stock }}件</div>
  </el-drawer>
</template>
<style scoped>
.imgcar {
  background-position: center center;
  background-repeat: no-repeat;
  width: 100%;
  height: 100%;
  background-size: cover;
}
</style>
