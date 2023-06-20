<script setup>
import SubmitBtn from './SubmitBtn.vue'
</script>

<template>
    <main class="flex justify-center items-center">
        <form action="" method="post" class="m-5 p-5">
            <div class="flex flex-col">
                <label for="default-input" class="block mb-2 font-medium">Input url:</label>
                <input placeholder="VideoUrl..." type="url" class="bg-white text-gray-900 text-sm rounded-xl ring-4 focus:ring-lime-400  block p-2 w-72 ">
                <SubmitBtn />
            </div>
        </form>
    </main>
</template>