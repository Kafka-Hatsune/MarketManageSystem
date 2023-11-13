<script setup>
import { useCounterStore } from '@/stores/counter.js'
const counterStore = useCounterStore()
</script>

<template>
  <div>
    <!-- 路由出口
    <router-view></router-view>
    <br />
    hello world -->
    {{ counterStore.count }}
    <button @click="counterStore.addCount">+</button>
  </div>
</template>

<style scoped></style>
