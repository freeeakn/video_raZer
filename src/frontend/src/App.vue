<script setup>

</script>

<template>
    <RouterView />
</template>

<style>
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
