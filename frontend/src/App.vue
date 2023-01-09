<template>
  <AppHeader/>
  <RouterView/>
  <AppFooter/>
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
  color: white;
  background-color: rgb(32, 32, 32);
}

html {
    background: rgb(32, 32, 32);
}

nav {
  a {
    font-weight: bold;
    color: #5999ff;

    &.router-link-exact-active {
      color: #ebebeb;
    }
  }
}
</style>
