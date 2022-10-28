<template>
  <div class="main">
    <h1>
      Welcome to DSA Web Application
    </h1>
    <p>
      This application contains several useful Data Structure and Algorithm tools.
    </p>
    <h3>Data Structure Tools</h3>
    <ul>
      <li><a href="/array">Array</a></li>
      <li><a href="/string">String</a></li>
      <li><a href="/linked-list">Linked List</a></li>
      <li><a href="/stack">Stack</a></li>
      <li><a href="/heap">Heap/Priority Queue</a></li>
      <li><a href="/tree">Tree</a></li>
      <li><a href="/graph">Graph</a></li>
      <li><a href="/advanced-graph">Advanced Graph</a></li>
      <li><a href="/interval">Interval</a></li>
    </ul>
    <h3>Algorithms</h3>
    <ul>
      <li><a href="/backtracking">Backtracking</a></li>
      <li><a href="/dynamic-programming">Dynamic Programming</a></li>
      <li><a href="/greedy-algorithm">Greedy Algorithm</a></li>
    </ul>
    <h3>Fundamental</h3>
    <ul>
      <li><a href="/math">Math & Geometry</a></li>
      <li><a href="/bit">Bit Manipulation</a></li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MainView',
  props: {
    msg: String
  }
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #5999ff;
}
</style>
