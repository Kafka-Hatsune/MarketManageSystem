<script setup>
defineOptions({
  name: 'HomeStatistic'
})
const props = defineProps({
  activeUser: Number,
  weeklyTrans: Number,
  productNum: Number,
  commentCount: Number
})
import { ChatLineRound, Finished } from '@element-plus/icons-vue'
</script>
<template>
  <el-row>
    <el-col :span="2"></el-col>
    <el-col :span="5">
      <el-statistic title="周活跃用户" :value="props.activeUser" />
    </el-col>
    <el-col :span="5">
      <el-statistic :value="props.weeklyTrans">
        <template #title>
          <div style="display: inline-flex; align-items: center">
            周交易量
            <el-icon style="margin-left: 4px" :size="12">
              <Finished />
            </el-icon>
          </div>
        </template>
      </el-statistic>
    </el-col>
    <el-col :span="5">
      <el-statistic title="当前在售商品数" :value="props.productNum" />
    </el-col>
    <el-col :span="5">
      <el-statistic title="评论总数" :value="props.commentCount">
        <template #suffix>
          <el-icon style="vertical-align: -0.125em">
            <ChatLineRound />
          </el-icon>
        </template>
      </el-statistic>
    </el-col>
    <el-col :span="2"></el-col>
  </el-row>
</template>
<style lang="scss" scoped>
.myBox {
  background-color: rgb(255, 255, 255);
  display: flex;
  justify-content: space-evenly;
}
</style>
