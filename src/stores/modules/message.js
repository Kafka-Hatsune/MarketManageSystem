import { ref } from 'vue'
import { defineStore } from 'pinia'

import {
  messageGetUnreadService,
  messageGetAllService,
  messageQueryUnreadService
} from '@/api/message'

export const useMessageStore = defineStore('message', () => {
  const messageList = ref([])
  const unreadMessageList = ref([])
  const ifHas = ref()

  const getUnreadMessageList = async () => {
    const res = await messageGetUnreadService()
    unreadMessageList.value = res.data.data
  }
  const getMessageList = async () => {
    const res = await messageGetAllService()
    messageList.value = res.data.data
  }
  const queryIfHasUnreadMessage = async () => {
    const res = await messageQueryUnreadService()
    ifHas.value = res.data.data.ifHas
  }
  return {
    messageList,
    unreadMessageList,
    ifHas,
    getUnreadMessageList,
    getMessageList,
    queryIfHasUnreadMessage
  }
})
