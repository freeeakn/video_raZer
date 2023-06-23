<script setup>
import { ref } from 'vue'
import axios from 'axios'
import router from '../../router'
import SubmitBtn from './SubmitBtn.vue'

const submit = ref(false);
const url = ref('');

const routerFunc = () => router.push('/answer');

const formSubmit = () => {

    let data = new FormData();
    data.append('url', url.value);
    data.append("csrfmiddlewaretoken", '{{csrf_token}}');
    
    submit.value = true;
    try {
        setTimeout(routerFunc, 3000);
        axios.get('answer/', data);
    } catch (err) {
        console.error(err.toJSON());
    }
};
</script>

<template>
    <main class="flex justify-center items-center">
        <form @submit.prevent.stop="formSubmit" class="m-5 p-5" v-if="!submit">
            <div class="flex flex-col">
                <label for="default-input" class="block mb-2 font-medium">Input url:</label>
                <input v-model="url" placeholder="VideoUrl..." type="url" name="url" class="bg-white text-gray-900 text-sm rounded-xl ring-4 focus:ring-lime-400  block p-2 w-72 drop-shadow-[0_35px_35px_rgb(163_230_53_/_0.09)]">
                <SubmitBtn />
            </div>
        </form>
        <div v-if="submit">
            <AppLoad />
        </div>
    </main>
</template>