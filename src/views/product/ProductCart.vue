<script setup>
import { onMounted, computed, ref } from 'vue'
import { useProductStore } from '@/stores'
import {
  productCartCountService,
  productCartDeleteService,
  productCartSettleService
} from '@/api/product'
import { ElMessage } from 'element-plus'
import router from '../../router'
const productStore = useProductStore()
onMounted(() => {
  productStore.getCartProducts()
})
const submitChange = async (productId, count) => {
  await productCartCountService({ productId, count })
  ElMessage.success('保存修改成功')
}
const jump2Details = (key) => {
  router.push(`/product/${key}`)
}
const sumPrice = computed(() => {
  return productStore.cartProductList.reduce((accumulator, obj) => {
    return accumulator + obj.count * obj.price
  }, 0)
})
const submitDelete = async (productId) => {
  await productCartDeleteService(productId)
  router.go(0)
}
const submitDeleteAll = async () => {
  for (const product of productStore.cartProductList) {
    await productCartDeleteService(product.productId)
  }
  ElMessage.success('成功清空购物车')
  router.go(0)
}
const callDialog = async () => {
  await productStore.getCartProducts()
  dialogFormVisible.value = true
}
const dialogFormVisible = ref(false)

const submitAllPurchase = async () => {
  await productCartSettleService()
  ElMessage.success('您的所有订单已创建成功')
  await productStore.getCartProducts()
}
</script>
<template>
  <span>共计 {{ sumPrice }}元</span>
  <el-button @click="submitDeleteAll">清空购物车</el-button>
  <el-button @click="callDialog">结算购物车</el-button>
  <el-row :gutter="20">
    <el-col
      :span="6"
      v-for="product in productStore.cartProductList"
      :key="product"
    >
      <el-card
        :body-style="{ padding: '0px' }"
        style="margin-top: 15px"
        class="hover-zoom"
      >
        <el-image
          :src="product.productPic"
          style="width: 100%; height: 200px"
        />
        <div style="padding: 14px">
          <span>{{ product.productName }}</span>
          <div class="price">
            <span class="price1">¥</span
            ><span class="price2">{{ product.price }}</span>
            <el-input-number
              v-model="product.count"
              :min="1"
              :max="product.stock"
              controls-position="right"
            />
          </div>
          <div>
            <span>小计 {{ product.count * product.price }} 元</span>
            <el-button @click="submitChange(product.productId, product.count)"
              >保存</el-button
            >
            <el-button @click="submitDelete(product.productId)"
              >移出购物车</el-button
            >
          </div>
          <div class="bottom">
            <time class="time">{{ product.createdTime }}</time>
            <el-button
              text
              class="button"
              @click.stop="jump2Details(product.productId)"
              >详情页</el-button
            >
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>

  <!-- 确定购物车对话框 -->
  <el-dialog v-model="dialogFormVisible" title="您的购物车">
    <el-row>
      <el-col :span="6">商品名</el-col>
      <el-col :span="6">商品单价</el-col>
      <el-col :span="6">购买商品数量</el-col>
      <el-col :span="6">小计</el-col>
    </el-row>
    <br />
    <el-row
      v-for="product in productStore.cartProductList"
      :key="product"
      style="line-height: 2"
    >
      <el-col :span="6">{{ product.productName }}</el-col>
      <el-col :span="6">{{ product.price }}</el-col>
      <el-col :span="6">{{ product.count }}</el-col>
      <el-col :span="6">{{ product.count * product.price }}</el-col>
    </el-row>
    <br />
    <el-row>
      <el-col :span="6"></el-col>
      <el-col :span="6"></el-col>
      <el-col :span="6"></el-col>
      <el-col :span="6">共计:{{ sumPrice }}元</el-col>
    </el-row>
    <!-- <ul>
      <li v-for="product in productStore.cartProductList" :key="product">
        {{ product.ProductName }}{{ product.price }}{{ product.count }}
      </li>
    </ul> -->
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="submitAllPurchase">
          结算购物车
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<style scoped>
.hover-zoom {
  width: auto;
  height: auto;
}
.hover-zoom:hover {
  transform: scale(1.05);
  transition: all 0.3s ease-in-out;
}
.center {
  margin-left: auto;
  margin-right: auto;
}
</style>
