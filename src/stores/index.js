import { createPinia } from 'pinia'
import persist from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(persist)

export default pinia
export * from './modules/user'
export * from './modules/product'
export * from './modules/order'
export * from './modules/statistic'
export * from './modules/message'
export * from './modules/promotion'