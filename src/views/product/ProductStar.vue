<script setup>
import { onMounted } from 'vue'
import { useProductStore } from '@/stores'

import ProductCard from '@/components/product/ProductCard.vue'
const productStore = useProductStore()
onMounted(() => {
  productStore.getStarredProducts()
})
</script>
<template>
  <el-row :gutter="20" class="el-row">
    <el-col
      :span="6"
      v-for="product in productStore.starProductList"
      :key="product"
    >
      <ProductCard :product="product" style="margin-top: 15px"></ProductCard>
    </el-col>
  </el-row>
</template>
