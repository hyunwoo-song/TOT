<template>
  <div>
    <ImgBanner imgSrc="https://source.unsplash.com/collection/190727/1600x900">
      <div style="line-height:1.2em;" slot="text">We will find a way.<br> We always have.</div>
    </ImgBanner>
    <v-container>
      <!-- About Me -->
      <v-layout my-5 justify-center>
        <v-flex xs8>
          <h2 class="headline mb-3 text-xs-center">About Me</h2>
          <p class="mr-4 text-xs-center">김호준(1993.10.14)<br/>경기대학교 컴퓨터과학과+융합보안학과<br/>SSAFY #1 구미 3반<br/>리그오브레전드 GOLD2<br/>오토체스 모바일 룩6</p>
        </v-flex>
        <v-flex xs4 hidden-xs-only>
          <v-img :src="getImgUrl('profile.png')" aspect-ratio="1.5"/>
        </v-flex>
      </v-layout>

      <!-- Youtube -->
      <v-layout my-5>
        <v-flex xs12>
          <h2 class="headline my-5 text-xs-center">Youtube</h2>
          <YoutubeList></YoutubeList>
        </v-flex>
      </v-layout>

      <!-- Portfolio -->
      <v-layout my-5>
        <v-flex xs12>
          <h2 class="headline my-5 text-xs-center">Portfolio</h2>
          <PortfolioList></PortfolioList>
        </v-flex>
      </v-layout>

      <!-- Post -->
      <v-layout my-5>
        <v-flex xs12>
          <h2 class="headline my-5 text-xs-center">Post</h2>
          <PostList :column="2"></PostList>
        </v-flex>
      </v-layout>


      <!-- Github -->
      <v-layout my-5>
        <v-flex xs12>
          <h2 class="headline my-5 text-xs-center">Project</h2>
          <RepositoryList></RepositoryList>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import PortfolioList from '../components/PortfolioList'
import PostList from '../components/PostList'
import RepositoryList from '../components/RepositoryList'
import YoutubeList from '../components/YoutubeList'

export default {
	name: 'HomePage',
	components: {
		ImgBanner,
		PortfolioList,
		PostList,
		RepositoryList,
    YoutubeList
	},
	methods: {
		getImgUrl(img) {
			return require('../assets/' + img);
		}
	},
}
</script>

<style>
  p {
    font-size : 2vw;
  }
</style>
