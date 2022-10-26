<template>
  <app-header/>
  <router-view/>
  <app-footer/>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'

export default {
  components: {
    AppHeader,
    AppFooter
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

nav {
  a {
    font-weight: bold;
    color: #042861;

    &.router-link-exact-active {
      color: #363636;
    }
  }
}
</style>
