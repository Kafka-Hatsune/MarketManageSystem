import { defineStore } from 'pinia'
import { ref } from 'vue'
import { productsService } from '../api/product'

export const useProductStore = defineStore('product', () => {
  // 声明数据
  const productList = ref({})
  // 声明操作数据的方法
  const getProducts = async () => {
    const res = await productsService()
    productList.value = res.data.data
  }
  return { productList, getProducts }
})
