import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'
export const useProductStore = defineStore('product', () => {
  // 声明数据
  const productList = ref([])
  // 声明操作数据的方法
  const getProducts = async () => {
    const {
      data: { data }
    } = await axios.get('')
    productList.value = data.productList // 根据接口去写
  }
  return { productList, getProducts }
})
