<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <MainView />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import MainView from '@/components/MainView.vue' // @ is an alias to /src

export default defineComponent({
  name: 'HomeView',
  components: {
    MainView
  }
})
</script>
