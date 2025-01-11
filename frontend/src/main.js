import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PrimeVue from 'primevue'
import 'primevue/resources/themes/lara-light-blue/theme.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'

const app = createApp(App)
app.use(router)
app.use(store)
app.use(PrimeVue, { ripple: true })
app.mount('#app')
