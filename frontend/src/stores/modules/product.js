import { defineStore } from 'pinia'
import { ref } from 'vue'
import { productGetAllInfoService } from '../../api/product'

export const useProductStore = defineStore('product', () => {
  // 声明数据
  const productList = ref({})
  // 声明操作数据的方法
  const getProducts = async () => {
    const res = await productGetAllInfoService()
    productList.value = res.data.data
  }
  return { productList, getProducts }
})
