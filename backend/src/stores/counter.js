import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // 声明数据
  const count = ref(0)
  const msg = ref('hello pinia')
  // 声明基于数据派生的计算属性
  const doubleCount = computed(() => count.value * 2)
  // 声明操作数据的 action
  const addCount = () => count.value++
  const subCount = () => count.value--

  return { count, msg, doubleCount, addCount, subCount }
})
