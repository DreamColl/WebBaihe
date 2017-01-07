<template>
  <div class="entry">
    <form action="post">
      <ol>
        <ul v-for="(item,index) in items">
          <!--input-->
          <a>{{ item.question }}</a><br v-if="item.type != 'select'">
          <input :type="item.type" v-if="item.type == 'input' "></input>
          <!--text-->
          <textarea :type="item.type" v-if="item.type == 'textarea' "></textarea>
          <!--select-->
          <select v-if="item.type == 'select' ">
            <option v-for="(op,index) in item.options">{{ op }}</option>
          </select>
          <!--checkbox-->
          <a v-if="item.type == 'checkbox' " :value="op" v-for="(op,index) in item.options">
            <label for="">{{ op }}</label>
            <input :type="item.type">
            </input>
          </a>
          <!--radio-->
          <a v-if="item.type == 'radio' " v-for="(op,index) in item.options" v-model="picked">
            <label :for="op">{{ op }}</label>
            <input :value="op" :name="item.question" :type="item.type">
            </input>
          </a>
          <!--file-->
          <input :type="item.type" v-if="item.type == 'file'">
        </ul>
      </ol>
    </form>
    <input type="submit">
  </div>
</template>
<script>
export default {
  name: 'entry',
  data() {
    return {
      items: data
    }
  },
  methods: {

  }
}

var data = [{
    type: 'input',
    question: '队名'
  },
  {
    type: 'textarea',
    question: '测试多行文本'
  },
  {
    type: 'select',
    question: '地区',
    options: ['华北', '东部', '中部', '西部', '东北']
  },
  {
    type: 'checkbox',
    question: '地区(复选)',
    options: ['华北', '东部', '中部', '西部', '东北'],
  },
  {
    type: 'radio',
    question: '地区（单选）',
    options: ['华北', '东部', '中部', '西部', '东北'],
    picked: '双向绑定TODO',
  },
  {
    type: 'file',
    question: '上传文件：',
  }
]
</script>
<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
ul{
  margin: 10px
}
</style>