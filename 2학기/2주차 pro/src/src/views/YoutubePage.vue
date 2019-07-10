<template>
  <div>
    <ImgBanner imgSrc="https://source.unsplash.com/5brvJbR1Pn8/1600x900">
      <div style="line-height:1.2em;font-size:1.2em;" slot="text">Youtube</div>
    </ImgBanner>
    <v-container>

      <!-- Post -->
      <v-layout>
        <v-flex xs12>
          <YoutubeList :limits="20"></YoutubeList>
        </v-flex>
      </v-layout>

    </v-container>
  </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import YoutubeList from '../components/YoutubeList'

export default {
	name: 'PostPage',
	components: {
		ImgBanner,
		YoutubeList,
	}
}
</script>
