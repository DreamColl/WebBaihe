<template lang="pug">
  .index 
    img(src="../assets/logo.png")
    .link-container
      router-link.link(:to="{name: 'announcement'}") 公告
      router-link.link(:to="{name: 'enter'}") 报名
</template>

<script lang="babel">
export default {
  name: 'index',
}
</script>

<style lang="stylus">
.index 
  text-align: center
  margin-top: 60px
  .link-container
    margin 100px
    .link
      margin 60px
      color: #000;
      text-decoration: none;
</style>