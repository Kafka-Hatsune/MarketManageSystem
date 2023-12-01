<script setup>
import { ref, onMounted } from 'vue'
import { useProductStore } from '@/stores'
import router from '@/router'
import { productModifyService } from '@/api/product'
import { ElMessage } from 'element-plus'
const productStore = useProductStore()
onMounted(() => {
  productStore.getProductTypes()
  productStore.getProduct(router.currentRoute.value.params.id)
  previewOldImages()
})

const imgUrls = new ref([])
let files = new ref()
const previewOldImages = () => {}

const previewImages = (event) => {
  imgUrls.value = []
  files = event.target.files
  if (files && files.length > 0) {
    for (let i = 0; i < files.length; i++) {
      const reader = new FileReader()
      reader.onload = (e) => {
        const imageData = e.target.result
        imgUrls.value.push(imageData)
      }
      reader.readAsDataURL(files[i])
    }
  }
}
const name = ref()
const typeValue = ref(productStore.product.typeName)
const price = ref()
const description = ref()
const stock = ref()
const onSubmit = async () => {
  console.log(
    typeValue.value,
    name.value,
    price.value,
    description.value,
    stock.value
  )
  let formData = new FormData()
  formData.append('productId', productStore.product.productId)
  formData.append('productPic', files)
  formData.append('typeName', typeValue)
  formData.append('productName', name)
  formData.append('price', price)
  formData.append('description', description)
  formData.append('stock', stock)
  await productModifyService(formData)
  // 提示用户
  ElMessage.success('成功修改商品')
  // 跳转到posted页面
  router.push('/product/posted')
}
</script>
<template>
  <!-- {{ productStore.product }} -->
  <!-- 表单 -->
  <el-form label-width="100px" style="max-width: 650px">
    <!-- 图片相关 -->
    <el-form-item label="商品图片">
      <div v-if="image in imgUrls">
        <img
          v-for="image in imgUrls"
          :src="image"
          :key="image"
          width="200"
          height="200"
        />
      </div>
      <div v-else>
        <img
          v-for="productPic in productStore.product.productPic"
          :key="productPic"
          :src="productPic"
          class="img"
        />
      </div>
      <input type="file" multiple @change="previewImages($event)" />
    </el-form-item>

    <!-- 商品名 -->
    <el-form-item label="商品名">
      <el-input
        v-model="name"
        :placeholder="productStore.product.productName"
      />
    </el-form-item>
    <!-- 商品种类 -->
    <el-form-item label="商品种类">
      <el-select
        v-model="typeValue"
        class="m-2"
        disabled
        :placeholder="productStore.product.typeName"
      >
        <el-option
          v-for="item in productStore.productTypeList"
          :key="item.typeName"
          :label="item.typeName"
          :value="item.typeName"
        />
      </el-select>
    </el-form-item>
    <!-- 商品价格 -->
    <el-form-item label="商品定价">
      <el-input-number
        v-model="price"
        :precision="2"
        :step="0.1"
        :min="0"
        controls-position="right"
        :placeholder="productStore.product.price"
      />
    </el-form-item>
    <!-- 库存 -->
    <el-form-item label="库存">
      <el-input-number
        v-model="stock"
        :step="1"
        :min="0"
        :placeholder="productStore.product.stock"
      />
    </el-form-item>
    <!-- 商品描述 -->
    <el-form-item label="商品描述">
      <el-input
        v-model="description"
        :autosize="{ minRows: 4 }"
        type="textarea"
        :placeholder="productStore.product.description"
      />
    </el-form-item>
    <!-- 提交表单 -->
    <el-form-item>
      <el-button type="primary" @click="onSubmit">修改商品</el-button>
    </el-form-item>
  </el-form>
</template>
<style scoped>
img {
  background-position: center center;
  background-repeat: no-repeat;
  width: 100%;
  height: 300px;
  background-size: cover;
}
</style>
