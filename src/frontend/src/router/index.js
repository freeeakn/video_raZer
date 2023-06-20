import { createRouter, createWebHistory } from 'vue-router'
import InputView from '../views/InputView.vue';
import OutputView from '../views/OutputView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'InputView',
      component: InputView
    },
    {
      path: '/answer',
      name: 'OutputView',
      component: OutputView
    },
  ]
})

export default router
