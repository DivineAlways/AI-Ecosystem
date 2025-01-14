import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'
import Card from 'primevue/card'
import Menubar from 'primevue/menubar'
import Timeline from 'primevue/timeline'
import Tag from 'primevue/tag'
import Tooltip from 'primevue/tooltip'
import Badge from 'primevue/badge'

import 'primevue/resources/themes/lara-light-blue/theme.css'
import 'primevue/resources/themes/lara-dark-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'

const app = createApp(App)

app.use(router)
app.use(store)
app.use(PrimeVue, { 
  ripple: true,
  inputStyle: 'filled'
})

app.component('Button', Button)
app.component('Card', Card)
app.component('Menubar', Menubar)
app.component('Timeline', Timeline)
app.component('Tag', Tag)
app.component('Badge', Badge)
app.directive('tooltip', Tooltip)

app.mount('#app')
