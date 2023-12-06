<script setup>
import { ref, onMounted } from 'vue'
import { useProductStore } from '@/stores'
import router from '@/router'
import { productCreateService } from '@/api/product'
import { ElMessage } from 'element-plus'
const productStore = useProductStore()
onMounted(() => {
  productStore.getProductTypes()
})

const imgUrls = new ref([])
let files = new ref([])
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
const typeValue = ref('')
const price = ref()
const description = ref()
const stock = ref()
// 经过验证 files为值
const onSubmit = async () => {
  console.log('这是files')
  console.log(files)
  console.log('这是value')
  console.log(files.length)
  let formData = new FormData()
  for (let i = 0; i < files.length; i++) {
    formData.append('productPic', files[i])
  }
  formData.append('typeName', typeValue.value)
  formData.append('productName', name.value)
  formData.append('price', price.value)
  formData.append('description', description.value)
  formData.append('stock', stock.value)
  await productCreateService(formData)
  // 提示用户
  ElMessage.success('成功发布商品')
  // 跳转到posted页面
  router.push('/product/posted')
}
</script>
<template>
  <!-- 表单 -->
  <el-form label-width="100px" style="max-width: 650px">
    <!-- 图片相关 -->
    <el-form-item label="商品图片">
      <div>
        <img
          v-for="image in imgUrls"
          :src="image"
          :key="image"
          width="200"
          height="200"
        />
      </div>
      <input type="file" multiple @change="previewImages($event)" />
    </el-form-item>

    <!-- 商品名 -->
    <el-form-item label="商品名">
      <el-input v-model="name" />
    </el-form-item>
    <!-- 商品种类 -->
    <el-form-item label="商品种类">
      <el-select v-model="typeValue" class="m-2">
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
      />
    </el-form-item>
    <!-- 库存 -->
    <el-form-item label="库存">
      <el-input-number v-model="stock" :step="1" :min="0" />
    </el-form-item>
    <!-- 商品描述 -->
    <el-form-item label="商品描述">
      <el-input
        v-model="description"
        :autosize="{ minRows: 2 }"
        type="textarea"
        placeholder="请输入商品描述"
      />
    </el-form-item>
    <!-- 提交表单 -->
    <el-form-item>
      <el-button type="primary" @click="onSubmit">发布商品</el-button>
    </el-form-item>
  </el-form>
</template>
