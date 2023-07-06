<script setup>
import Header from "./components/Header.vue"
import Footer from "./components/Footer.vue"
</script>

<template>
  <div class="bg-gray-900 text-white">
        <div class="animation flex flex-col justify-around h-screen w-full">
          <Header />
          
          <Footer />
        </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@300;500;800;900&display=swap');
* {
    font-family: 'Mulish', sans-serif;
}
</style>
