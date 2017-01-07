<template>
  <form action="post">
    <div class="entry">
      <div v-for="(item,index) in items">
        <a>{{ item.question }}</a>
        <input v-bind:type="item.type" ></input>
      </div>
    </div>
  </form>
</template>
<script>
export default {
  name: 'entry',
  data() {
    return {
      items: [{
          type: 'input',
          question: '队名'
        },
        {
          type: 'input',
          question: '队名'
        }
      ]
    }
  }
}
</script>