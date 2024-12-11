<script setup>
import Banner from './components/Banner.vue';
import NavBar from './components/NavBar.vue';
import Filter from './components/Filter.vue'
import Item from './components/Item.vue'

</script>

<template>
  <NavBar />
  <Banner />
  <div class="px-5">
    <Filter />
  </div>
  <div class="flex justify-center">
    <Item />
  </div>

</template>

<style scoped></style>
