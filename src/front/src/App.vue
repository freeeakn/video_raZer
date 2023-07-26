<script setup>
import Header from "./components/Header.vue"
import Footer from "./components/Footer.vue"
import AppLoad from "./components/AppLoad.vue"
import { reactive, ref } from 'vue'
import axios from 'axios'

const submit = ref(false);
const output = ref(false);
const url = ref('');
const answer = reactive({});

const formSubmit = () => {

    let data = new FormData();
    data.append('url', url.value);
    data.append('csrfmiddlewaretoken', '{{csrf_token}}');
    
    submit.value = true;
    try {
      setTimeout(() => {
          output.value = true;
          submit.value = false;
        }, 3000);
        axios.post('api/', data)
            .then(response => {
              answer = response
            })
            .catch(error => {
              answer = {err: 'Error: ' + error.response.status}
            })
    } catch (err) {
        console.error(err.toJSON());
    }
};
</script>

<template>
  <div class="bg-gray-900 text-white">
        <div class="animation flex flex-col justify-around h-screen w-full">
          <Header />
          <main class="flex justify-center items-center">
              <form @submit.prevent.stop="formSubmit" class="m-5 p-5" v-if="(!output && !submit)">
                  <div class="flex flex-col">
                      <label for="default-input" class="block mb-2 font-medium">Input url:</label>
                      <input v-model="url" placeholder="VideoUrl..." type="url" name="url" class="bg-white text-gray-900 text-sm rounded-xl ring-4 focus:ring-lime-400  block p-2 w-72 drop-shadow-[0_35px_35px_rgb(163_230_53_/_0.09)]">
                  </div>
              </form>
              <div v-if="submit">
                  <AppLoad />
              </div>
          </main>

          <main class="flex flex-col items-center justify-center p-5" v-if="output">
              <div class="m-2 p-2 xl:w-1/2 drop-shadow-[0_20px_20px_rgb(163_230_53_/_0.15)]">
                  <section  class="mb-16">
                      <img class="w-full mb-5" src="https://randompicturegenerator.com/img/national-park-generator/gebf2d43a7afe4f731303406b059dd0aeed652937b8880225bbaf7c8b064374526b88012f8f26cc7883954cebc4f02996_640.jpg" alt="screenShot">
                      <a href="#">{{ answer.start }}</a>
                      <p>
                          {{ answer.text }}
                      </p>
                  </section>
              </div>
              <button @click="() => {
                output = false;
                submit = false;
              }">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" />
                </svg>
              </button>
          </main>

          <Footer />
        </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@300;500;800;900&display=swap');
* {
    font-family: 'Mulish', sans-serif;
}

.animation {
  transform: scale(0.75);
  opacity: 0;
  animation: ani 1s forwards;
}

@keyframes ani {
  0% {
    transform: scale(0.75);
    opacity: 0;
}
  100% {
    opacity: 1;
    transform: scale(1);
}
}
</style>
