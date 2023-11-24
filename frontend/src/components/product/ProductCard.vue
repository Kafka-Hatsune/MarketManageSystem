<script setup>
import { useRouter } from 'vue-router'
defineOptions({
  name: 'ProductCard'
})
const props = defineProps({
  product: {}
})
const router = useRouter()
// const productId = props.product.productId
const jump2Details = (key) => {
  router.push(`/product/${key}`)
}
</script>
<template>
  <el-card
    :body-style="{ padding: '0px' }"
    @click.stop="jump2Details(props.product.productId)"
    class="hover-zoom"
  >
    <img :src="props.product.productPic[0]" class="image" />
    <div style="padding: 14px">
      <span>{{ props.product.ProductName }}</span>
      <div class="price">
        <span class="price1">¥</span
        ><span class="price2">{{ props.product.price }}</span>
      </div>
      <div class="bottom">
        <time class="time">{{ props.product.createdTime }}</time>
        <el-button
          text
          class="button"
          @click.stop="jump2Details(props.product.productId)"
          >去看看</el-button
        >
      </div>
    </div>
  </el-card>
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
.price {
  display: flex;
  justify-content: flex-end;
}
.price1 {
  color: rgb(255, 80, 0);
  font-size: medium;
}
.price2 {
  color: rgb(255, 80, 0);
  font-size: large;
}
.image {
  width: 250px;
  height: 250px;
}

.time {
  font-size: 12px;
  color: #999;
}
.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
