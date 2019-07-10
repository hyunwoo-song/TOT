<template>
  <div>
    <ImgBanner imgSrc="https://source.unsplash.com/5brvJbR1Pn8/1600x900">
      <div style="line-height:1.2em;font-size:1.2em;" slot="text">Portfolio Detail</div>
    </ImgBanner>
    <v-container>
      <v-card>
        <v-img :src="imgSrc" height="auto">
        </v-img>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{title}}</div>
            <span class="grey--text">{{body}}</span>
          </div>
        </v-card-title>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'

export default {
	name: 'PortfolioDetailPage',
	components: {
		ImgBanner
	},
  data() {
    return {
        title : '',
        date : '',
        imgSrc : '',
        body :  ''
    }
  },
  mounted() {
    this.$data.title = this.$route.params.portfolioInfo.title;
    this.$data.date = this.$route.params.portfolioInfo.date;
    this.$data.imgSrc = this.$route.params.portfolioInfo.imgSrc;
    this.$data.body = this.$route.params.portfolioInfo.body;
  }
}
</script>
