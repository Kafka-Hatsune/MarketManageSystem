<script setup>
import { useCounterStore } from '@/stores/counter.js'
const counterStore = useCounterStore()

import { useProductStore } from '@/stores/product.js'
import { onMounted } from 'vue'
const productStore = useProductStore()

onMounted(() => {
  productStore.getProducts()
})
</script>

<template>
  <div>
    <!-- 路由出口
    <router-view></router-view>
    <br />
    hello world -->
    {{ counterStore.count }}
    <button @click="counterStore.addCount">+</button>
    <br />
    <!-- productStore.getProducts()
    {{ productStore.getProducts() }} -->
    <br />
    productStore.productList
    {{ productStore.productList }}
  </div>
</template>

<style scoped></style>
