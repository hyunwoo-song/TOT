<template>
  <div>
    <ImgBanner imgSrc="https://source.unsplash.com/5brvJbR1Pn8/1600x900">
      <div style="line-height:1.2em;font-size:1.2em;" slot="text">Post</div>
    </ImgBanner>
    <v-container>
      이미지 업로드 컴포넌트 테스트
      <v-flex>
        <ImgUpload></ImgUpload>
      </v-flex>
      이미지 다운로드 컴포넌트 테스트
      <v-flex>
        <Gallery/>
      </v-flex>
    </v-container>
  </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import ImgUpload from '../components/ImgUpload'
import Gallery from '../components/Gallery'

export default {
	name: 'PostPage',
	components: {
		ImgBanner,
		ImgUpload,
    Gallery
	}
}
</script>
