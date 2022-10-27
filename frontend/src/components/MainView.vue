<template>
  <div class="main">
    <h1>
      Welcome to DSA Web Application
    </h1>
    <p>
      This application contains several useful Data Structure and Algorithm tools.
    </p>
    <h3>Arrays/Hashing</h3>
    <ul>
      <li><a href="https://leetcode.com/problems/contains-duplicate/" target="_blank" rel="noopener">Contains Duplicate (Coming Soon)</a></li>
    </ul>
    <h3>Strings</h3>
    <ul>
      <li><a href="">Valid Palindrome (Coming Soon)</a></li>
    </ul>
    <h3>Stack</h3>
    <ul>
      <li><a href="">Valid Parenthesis (Coming Soon)</a></li>
    </ul>
    <h3>Binary Search</h3>
    <h3>Linked List</h3>
    <h3>Trees</h3>
    <h3>Tries</h3>
    <h3>Heap/Priority Queue</h3>
    <h3>Backtracking</h3>
    <h3>Graphs</h3>
    <h3>Advanced Graphs</h3>
    <h3>Dynamic Programming</h3>
    <h3>Greedy Algorithms</h3>
    <h3>Intervals</h3>
    <h3>Math & Geometry</h3>
    <h3>Bit Manipulation</h3>
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
