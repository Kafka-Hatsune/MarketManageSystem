import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
  productGetAllInfoService,
  productGetProductDetailService,
  productGetTypeService,
  productGetPostedService,
  productIfStarService,
  productGetStarService,
  productGetCartService,
  productCartSelectService
} from '../../api/product'

export const useOrderStore = defineStore('product', () => {
  // 声明数据
  const productList = ref({})
  const product = ref({})
  const productTypeList = ref([])
  const postProductList = ref([])
  const sales_quantity = ref()
  const sales_volume = ref()
  const productIfStar = ref()
  const starProductList = ref([])
  const cartProductList = ref([])
  const productIfCart = ref()
  // 声明操作数据的方法
  const getProducts = async () => {
    const res = await productGetAllInfoService()
    productList.value = res.data.data
  }
  const getProduct = async (id) => {
    const res = await productGetProductDetailService(id)
    console.log(res)
    product.value = res.data.data
  }
  const getProductTypes = async () => {
    const res = await productGetTypeService()
    productTypeList.value = res.data.data
  }
  const getPostedProducts = async () => {
    const res = await productGetPostedService()
    postProductList.value = res.data.data
    sales_quantity.value = postProductList.value.reduce((accumulator, obj) => {
      return accumulator + obj.sale
    }, 0)
    sales_volume.value = postProductList.value.reduce((accumulator, obj) => {
      return accumulator + obj.sale * obj.price
    }, 0)
  }
  const getStarredProducts = async () => {
    const res = await productGetStarService()
    starProductList.value = res.data.data
  }
  const checkIfStarred = async (id) => {
    const res = await productIfStarService(id)
    productIfStar.value = res.data.data
  }
  const getCartProducts = async () => {
    const res = await productGetCartService()
    cartProductList.value = res.data.data
  }
  const checkIfCart = async (id) => {
    const res = await productCartSelectService(id)
    productIfCart.value = res.data.data
  }
  return {
    productList,
    product,
    getProducts,
    getProduct,
    productTypeList,
    getProductTypes,
    postProductList,
    getPostedProducts,
    sales_quantity,
    sales_volume,
    checkIfStarred,
    productIfStar,
    getStarredProducts,
    starProductList,
    getCartProducts,
    cartProductList,
    checkIfCart,
    productIfCart
  }
})




/*
import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
    orderGetConsumer,
    orderGetSeller
} from '../../api/order'

export const useOrderStore = defineStore('order', () => {
  // 声明数据
  const OrderSellerList = ref({})
  const OrderConsumerList = ref({})
  //const product = ref({})
  //const productTypeList = ref([])
  //const postProductList = ref([])
  //const sales_quantity = ref()
  //const sales_volume = ref()
  //const productIfStar = ref()
  //const starProductList = ref([])
  //const cartProductList = ref([])
  //const productIfCart = ref()
  // 声明操作数据的方法
  const getOrderSeller = async () => {
    const res = await orderGetSeller()
    OrderSellerList.value = res.data.data
  }
  const getOrderConsumer = async () => {
    const res = await orderGetConsumer()
    OrderConsumerList.value = res.data.data
  }
  //const getProducts = async () => {
  //  const res = await productGetAllInfoService()
  //  productList.value = res.data.data
  //}
  //const getProduct = async (id) => {
  //  const res = await productGetProductDetailService(id)
  //  console.log(res)
  //  product.value = res.data.data
  //}
  //const getProductTypes = async () => {
  //  const res = await productGetTypeService()
  //  productTypeList.value = res.data.data
  //}
  //const getPostedProducts = async () => {
  //  const res = await productGetPostedService()
  //  postProductList.value = res.data.data
  //  sales_quantity.value = postProductList.value.reduce((accumulator, obj) => {
  //    return accumulator + obj.sale
  //  }, 0)
  //  sales_volume.value = postProductList.value.reduce((accumulator, obj) => {
  //    return accumulator + obj.sale * obj.price
  //  }, 0)
  //}
  //const getStarredProducts = async () => {
  //  const res = await productGetStarService()
  //  starProductList.value = res.data.data
  //}
  //const checkIfStarred = async (id) => {
  //  const res = await productIfStarService(id)
  //  productIfStar.value = res.data.data
  //}
  //const getCartProducts = async () => {
  //  const res = await productGetCartService()
  //  cartProductList.value = res.data.data
  //}
  //const checkIfCart = async (id) => {
  //  const res = await productCartSelectService(id)
  //  productIfCart.value = res.data.data
  //}
  return {
    OrderSellerList,
    OrderConsumerList,
    getOrderSeller,
    getOrderConsumer
  }
})
*/