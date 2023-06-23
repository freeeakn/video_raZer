<script setup>
import axios from 'axios'

const response = axios.get('getApi/');
console.log(response);

</script>

<template>
    <main class="flex flex-col items-center justify-center p-5">
        <div class="m-2 p-2 xl:w-1/2 drop-shadow-[0_20px_20px_rgb(163_230_53_/_0.15)]">
            <!-- {% for item in data %} -->
            <section  class="mb-16">
                <!-- <img class="w-full mb-5" src="https://randompicturegenerator.com/img/national-park-generator/gebf2d43a7afe4f731303406b059dd0aeed652937b8880225bbaf7c8b064374526b88012f8f26cc7883954cebc4f02996_640.jpg" alt="screenShot"> -->
                <a href="#">{{ start }}</a>
                <p>
                    {{ text }}
                </p>
            </section>
            <!-- {% endfor %} -->
        </div>
        <router-link to="/">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" />
        </svg>
        </router-link>
    </main>
</template>