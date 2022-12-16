<template>
    <h1>Array</h1>

    <h3> Input: </h3>
    <textarea @input="updateInput($event.target.value)" rows="2" cols="50">1,2,3,4</textarea>

    <h3>Tools:</h3>
    <button type="button" @click="containsDuplicate">Contains Duplicate</button>
    <button type="button">Valid Anagram</button>
    <button type="button">Two Sum</button>
    <button type="button">Group Anagrams</button>
    <button type="button">Top K Frequent Elements</button>
    <button type="button">Product of Array Except Self</button>
    <button type="button">Valid Sudoku</button>
    <button type="button">Encode and Decode Strings</button>
    <button type="button">Longest Consecutive Sequence</button>

    <h3>Output:</h3>
    <textarea v-html="output" rows="2" cols="50" readonly></textarea>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      input: '1,2,3,4',
      output: 'Results will go here...'
    }
  },
  methods: {
    async containsDuplicate () {
      const response = await axios.get(`http://localhost:8000/array/contains-duplicate/?arr=${this.input}`)
      this.output = response.data
    },
    updateInput (value) {
      this.input = value
    }
  }
}
</script>

<style lang="scss">
button {
  margin: 5px 5px 5px 5px;
  background-color: #e7e7e7;
  border: none;
  border-radius: 12px;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor:pointer;
}

button:hover {
  background-color: #7e7e7e;
  color: white;
}

textarea {
    padding: 10px;
    max-width: 100%;
    line-height: 1.5;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-shadow: 1px 1px 1px #999;
}
</style>
