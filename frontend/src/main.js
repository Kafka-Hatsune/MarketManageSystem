import './assets/main.scss'

import { createApp } from 'vue'
import App from './App.vue'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import pinia from './stores'
import router from './router'

const app = createApp(App)

app.use(pinia)
app.use(router)
app.use(ElementPlus)

app.mount('#app')
