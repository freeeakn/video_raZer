import { createApp } from 'vue'
import App from './App.vue'
import AppHeader from './components/global/AppHeader.vue'
import AppFooter from './components/global/AppFooter.vue'
import AppForm from './components/global/AppForm.vue'
import AppPopUp from './components/global/AppPopUp.vue'

import './assets/tailwind.css'

const app = createApp(App);

app
    .component('AppHeader', AppHeader)
    .component('AppFooter', AppFooter)
    .component('AppForm', AppForm)
    .component('AppPopUp', AppPopUp)


app.mount('#app');
