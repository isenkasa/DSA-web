<template>
    <h1>Array</h1>

    <p>An array is a collection of similar data elements stored at contiguous memory locations. It is the simplest data structure where each data element can be accessed directly by only using its index number <a href="https://www.mygreatlearning.com/blog/what-is-an-array-learn-more-in-one-read/" target="__blank">(Reference)</a>.</p>

    <p><strong>Time complexity:</strong></p>
    <table>
      <tbody>
        <tr>
          <td><strong>Algorithm</strong></td>
          <td><strong>Average case</strong></td>
          <td><strong>Worst case</strong></td>
        </tr>
        <tr>
          <td><strong>Access</strong></td>
          <td>O(1)</td>
          <td>O(1)</td>
        </tr>
        <tr>
          <td><strong>Search</strong></td>
          <td>O(n)</td>
          <td>O(n)</td>
        </tr>
        <tr>
          <td><strong>Insertion</strong></td>
          <td>O(n)</td>
          <td>O(n)</td>
        </tr>
        <tr>
          <td><strong>Deletion</strong></td>
          <td>O(n)</td>
          <td>O(n)</td>
        </tr>
      </tbody>
    </table>

    <h3>Input:</h3>
    <textarea @input="updateInput($event.target.value)" rows="2" cols="50">1,2,3,4</textarea>

    <h3>Tools:</h3>
    <button type="button" @click="containsDuplicate">Contains Duplicate</button>

    <h2>More coming soon...</h2>

    <!--
    <button type="button">Valid Anagram</button>
    <button type="button">Two Sum</button>
    <button type="button">Group Anagrams</button>
    <button type="button">Top K Frequent Elements</button>
    <button type="button">Product of Array Except Self</button>
    <button type="button">Valid Sudoku</button>
    <button type="button">Encode and Decode Strings</button>
    <button type="button">Longest Consecutive Sequence</button>
    -->

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
      try {
        const response = await axios.get(`http://localhost:8000/array/contains-duplicate/?arr=${this.input}`)
        this.output = response.data
      } catch (error) {
        this.output = 'Server Error - Please make sure your input is correct!'
      }
    },
    updateInput (value) {
      this.input = value
    }
  }
}
</script>

<style lang="scss">
table {
  border: 1px solid white;
  display: inline-block;
}

td {
  text-align: left;
}

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
