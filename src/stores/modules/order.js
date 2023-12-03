//*
import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
  productGetAllInfoService,
  productGetProductDetailService,
  productGetTypeService,
  productGetPostedService,
} from '../../api/product'
import {
  orderGetConsumer,
  orderGetSeller
} from '../../api/order'

export const useOrderStore = defineStore('order', () => {
  // 声明数据
  const orderSellerList = ref({})
  const orderConsumerList = ref({})
  // 声明操作数据的方法
  const getOrderSeller = async () => {
    const res = await orderGetSeller()
    orderSellerList.value = res.data.data
  }
  const getOrderConsumer = async () => {
    const res = await orderGetConsumer()
    orderConsumerList.value = res.data.data
  }
  return {
    orderSellerList,
    orderConsumerList,
    getOrderSeller,
    getOrderConsumer
  }
})