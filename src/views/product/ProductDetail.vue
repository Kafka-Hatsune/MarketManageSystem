<script setup>
import { useProductStore, useUserStore } from '@/stores'
import { onMounted, ref, toRef } from 'vue'
import { commentSubmitService } from '@/api/comment'
import {
  productPurchaseService,
  productStarNewService,
  productCartNewService,
  productCartDeleteService
} from '@/api/product'
import { ElMessage } from 'element-plus'
import router from '@/router'
import avatar from '@/assets/user/default.png'
const productStore = useProductStore()
const routeId = router.currentRoute.value.params.id
onMounted(() => {
  productStore.getProduct(routeId)
  productStore.checkIfStarred(routeId)
  productStore.checkIfCart(routeId)
  userStore.getCurRecInfor()
})
const productId = toRef(routeId)
const commentText = ref()
const submitCommentForm = ref({
  commentText,
  productId
})
const submitComment = async () => {
  await commentSubmitService(submitCommentForm.value)
  ElMessage.success('创建评论成功')
  await productStore.getProduct(routeId)
}
const count = ref(1)
const submitPurchaseForm = ref({
  productId,
  count
})
const submitPurchase = async () => {
  console.log(submitPurchaseForm.value)
  await productPurchaseService(submitPurchaseForm.value)
  ElMessage.success('成功创建订单')
  dialogFormVisible.value = false
}
const switchStar = async () => {
  await productStarNewService(routeId)
  await productStore.checkIfStarred(routeId)
}
const submitCart = async (productId, count) => {
  await productCartNewService({ productId, count })
  await productStore.checkIfCart(routeId)
}
const submitDelete = async (productId) => {
  await productCartDeleteService(productId)
  router.go(0)
}
const userStore = useUserStore()
const dialogFormVisible = ref(false)
const callDialog = async () => {
  console.log(dialogFormVisible)
  await userStore.getCurRecInfor()
  dialogFormVisible.value = true
  console.log(dialogFormVisible)
  // await userStore.getCurRecInfor()
}
</script>
<template>
  <!-- {{ productStore.productIfStar }} -->

  <el-row>
    <el-col :span="16">
      <el-row>
        <el-col :span="2"></el-col>
        <el-col :span="20">
          <el-carousel class="carousel">
            <el-carousel-item
              v-for="productPic in productStore.product.productPic"
              :key="productPic"
            >
              <img :src="productPic" class="imgcar" />
            </el-carousel-item>
          </el-carousel>
        </el-col>
        <el-col :span="2"></el-col>
      </el-row>
      <el-row>
        <el-col :span="2"></el-col>
        <el-col :span="20">
          <h1>商品评论</h1>
          <el-input
            v-model="commentText"
            :autosize="{ minRows: 2, maxRows: 5 }"
            type="textarea"
            clearable
            placeholder="新增评论"
          />
          <el-button @click="submitComment">提交</el-button>
          <ul class="ul-comment">
            <li
              class="li-comment"
              v-for="comment in productStore.product.comments"
              :key="comment.createdTime"
            >
              <el-row>
                <el-avatar :src="comment.publisher.avatar || avatar" />
                <span style="height: line-height">
                  {{ comment.publisher.userName }}</span
                >
              </el-row>
              <div>{{ comment.text }}</div>
              <div>
                <label style="color: #aaaaaa">{{ comment.createdTime }}</label>
              </div>
              <br />
            </li>
          </ul>
        </el-col>
        <el-col :span="2"></el-col>
      </el-row>
    </el-col>
    <el-col :span="8">
      <h1 class="title">{{ productStore.product.productName }}</h1>
      <ul class="ul-message">
        <li class="li-message">
          <div><span>价格:</span> {{ productStore.product.price }}</div>
        </li>
        <li class="li-message">
          <div>商品种类: {{ productStore.product.typeName }}</div>
        </li>
        <li class="li-message">
          <section>商品描述: {{ productStore.product.description }}</section>
        </li>
        <li class="li-message">剩余库存: {{ productStore.product.stock }}件</li>
        <li class="li-message">
          数量:
          <el-input-number
            v-model="count"
            :min="1"
            :max="productStore.product.stock"
          />
          件
        </li>
        <li>
          <span>
            <el-button
              v-if="
                productStore.productIfStar &&
                productStore.productIfStar.ifStarred
              "
              @click="switchStar"
              >取消收藏</el-button
            >
            <el-button v-else @click="switchStar">收藏</el-button>
          </span>

          <span>
            <el-button
              v-if="
                productStore.productIfCart && productStore.productIfCart.ifCart
              "
              @click="submitDelete(productStore.product.productId)"
              >清空该购物车项</el-button
            >
            <el-button
              v-else
              @click="submitCart(productStore.product.productId, count)"
              >添加购物车</el-button
            ></span
          >
        </li>
        <li class="li-message">
          <el-button @click="callDialog()"> 购买</el-button>
          <!-- <el-button @click="submitPurchase"> 购买 </el-button> -->
        </li>
      </ul>
    </el-col>
  </el-row>
  <!-- 确认购买对话框 -->
  <el-dialog v-model="dialogFormVisible" title="请确认收货信息">
    <el-form :model="form" v-if="userStore.curRecInfor">
      <el-form-item label="收货人姓名" :label-width="formLabelWidth">
        <el-input v-model="userStore.curRecInfor.name" disabled />
      </el-form-item>
      <el-form-item label="收货人电话" :label-width="formLabelWidth">
        <el-input v-model="userStore.curRecInfor.phone" placeholder disabled />
      </el-form-item>
      <el-form-item label="收货人地址" :label-width="formLabelWidth">
        <el-input v-model="userStore.curRecInfor.place" placeholder disabled />
      </el-form-item>
    </el-form>
    <div v-else>快去设置你的收货地址</div>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button
          v-if="userStore.curRecInfor"
          type="primary"
          @click="submitPurchase"
        >
          确认购买
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<style scoped>
.carousel {
  padding: 20px 0 20px 0;
}
.imgcar {
  background-position: center center;
  background-repeat: no-repeat;
  width: 100%;
  height: 300px;
  background-size: cover;
}
.title {
  text-align: center;
  min-height: 21px;
  _height: 21px;
  font-size: 16px;
  font-weight: 700;
  line-height: 21px;
  color: #3c3c3c;
}
.ul-message {
  padding: 0;
  list-style-type: none;
}
.li-message {
  height: auto;
  margin: 20px 0;
}
.ul-comment {
  padding: 0;
}
.li-comment {
  list-style-type: none;
}
</style>
