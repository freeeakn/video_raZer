import './assets/tailwind.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import AppHeader from './components/global/AppHeader.vue'
import AppFooter from './components/global/AppFooter.vue'
import AppForm from './components/global/AppForm.vue'
import AppPopUp from './components/global/AppPopUp.vue'
import AppAnswer from './components/global/AppAnswer.vue'

axios.defaults.baseURL = 'http://127.0.0.1:8000';

const app = createApp(App);

app.use(router, axios);

app
    .component('AppHeader', AppHeader)
    .component('AppFooter', AppFooter)
    .component('AppForm', AppForm)
    .component('AppPopUp', AppPopUp)
    .component('AppAnswer', AppAnswer)

app.mount('#app');
