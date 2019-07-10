<template>
  <v-card :to="{name:'portfolioDetail', params: {portfolioInfo : $data.portfolioInfo}}">
    <v-img :src="imgSrc" height="200px">
    </v-img>
    <v-card-title primary-title>
      <div>
        <div class="headline" v-line-clamp="1">{{title}}</div>
        <span class="grey--text" v-line-clamp="4">{{body}}</span>
      </div>
    </v-card-title>
  </v-card>
</template>

<script>
export default {
	name: 'Portfolio',
	props: {
		date: {type: String},
		title: {type: String},
		body: {type: String},
		imgSrc: {type: String},
	},
  data(){
    return {
      portfolioInfo : {
        date: {type: String},
  		  title: {type: String},
  		  body: {type: String},
  		  imgSrc: {type: String}
      }
    }
  },
  mounted(){
    this.$data.portfolioInfo.date = this.$props.date;
    this.$data.portfolioInfo.title = this.$props.title;
    this.$data.portfolioInfo.body = this.$props.body;
    this.$data.portfolioInfo.imgSrc = this.$props.imgSrc;
  }
}
</script>
