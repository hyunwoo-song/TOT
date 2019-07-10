<template>
  <div>
    <iframe :src='url' height="200px" width="300px" allow="autoplay"></iframe>
  </div>
</template>

<script>
    export default{
      name: 'youtube',
      props: {
        url : {type: null}
      }
    }
</script>
