import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
  promotionGetAllService,
  promotionGetActiveService
} from '@/api/promotion'

export const usePromotionStore = defineStore('promotion', () => {
  const promotionList = ref([])
  const promotionActiveList = ref([])
  const getPromotionList = async () => {
    const res = await promotionGetAllService()
    promotionList.value = res.data.data
  }
  const getPromotionActiveList = async () => {
    const res = await promotionGetActiveService()
    promotionActiveList.value = res.data.data
  }
  const ifShow = ref(true)
  return {
    promotionList,
    promotionActiveList,
    getPromotionList,
    getPromotionActiveList,
    ifShow
  }
})
