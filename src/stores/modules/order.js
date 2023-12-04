//*
import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
  orderGetConsumer,
  orderGetSeller,
  orderGetAllService
} from '@/api/order'

export const useOrderStore = defineStore('order', () => {
  // 声明数据
  const orderSellerList = ref([])
  const orderConsumerList = ref([])

  const orderList = ref([])
  // 声明操作数据的方法
  const getOrderSeller = async () => {
    const res = await orderGetSeller()
    orderSellerList.value = res.data.data
  }
  const getOrderConsumer = async () => {
    const res = await orderGetConsumer()
    orderConsumerList.value = res.data.data
  }
  const getOrderList = async () => {
    const res = await orderGetAllService()
    orderList.value = res.data.data
  }
  return {
    orderSellerList,
    orderConsumerList,
    getOrderSeller,
    getOrderConsumer,
    getOrderList,
    orderList
  }
})
