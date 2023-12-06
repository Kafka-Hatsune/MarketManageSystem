import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
  statisticGetActiveUserService,
  statisticGetProductCountService,
  statisticGetCommentCountService,
  statisticGetActiveOrderCountService
} from '@/api/statistic'

export const useStatisticStore = defineStore('statistic', () => {
  const activeUserCount = ref()
  const productCount = ref()
  const commentCount = ref()
  const activeOrderCount = ref()
  const getActiveUserCount = async () => {
    const res = await statisticGetActiveUserService()
    activeUserCount.value = res.data.data.number
  }
  const getProductCount = async () => {
    const res = await statisticGetProductCountService()
    productCount.value = res.data.data.number
  }
  const getCommentCount = async () => {
    const res = await statisticGetCommentCountService()
    commentCount.value = res.data.data.number
  }
  const getActiveOrderCount = async () => {
    const res = await statisticGetActiveOrderCountService()
    activeOrderCount.value = res.data.data.number
  }
  return {
    activeUserCount,
    productCount,
    commentCount,
    activeOrderCount,
    getActiveUserCount,
    getProductCount,
    getCommentCount,
    getActiveOrderCount
  }
})
