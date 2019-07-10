<template>
  <div>
  <!-- header -->
  <v-toolbar color="indigo" fixed>
    <v-toolbar-side-icon :to="{name:'home'}"><v-icon>fa fa-home</v-icon></v-toolbar-side-icon>
    <v-btn color="flat" icon @click="popUpMessage"><v-icon>fa fa-star</v-icon></v-btn>

    <!-- title -->
    <template>
      <v-toolbar-title class="white--text"> 명세서 보고 따라한 블로그 </v-toolbar-title>
    </template>
    <v-spacer></v-spacer>
    <!-- header menu -->
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat small color="white" :to="{name:'youtube'}">Youtube</v-btn>
      <v-btn flat small color="white" :to="{name:'portfolio'}">Portfolio</v-btn>
      <v-btn flat small color="white" :to="{name:'post'}">Post</v-btn>
      <v-btn flat small color="white" :to="{name:'login'}">login</v-btn>
    </v-toolbar-items>

    <!-- side menu button -->
    <v-btn flat small color="white" class="hidden-md-and-up" @click="active=!active"><v-icon>fa fa-bars</v-icon></v-btn>
    <div id="parentx">
      <vs-sidebar parent="body" default-index="1" class="sidebarx" spacer v-model="active">
        <div class="header-sidebar" slot="header">
          <vs-avatar  size="70px" :src="getImgUrl('profile2.png')" />
          <h4> 김호준 </h4>
        </div>

        <!-- side menu items -->
        <vs-sidebar-item index="1" icon="photo_library" :to="{name:'youtube'}"> Youtube </vs-sidebar-item>
        <vs-sidebar-item index="2" icon="photo_library" :to="{name:'portfolio'}"> Portfolio </vs-sidebar-item>
        <vs-sidebar-item index="3" icon="edit" :to="{name:'post'}"> Post </vs-sidebar-item>
        <vs-sidebar-item index="4" icon="account_circle" :to="{name:'login'}"> Login </vs-sidebar-item>

        <div class="footer-sidebar" slot="footer">
          <vs-button icon="reply" color="danger" type="flat">log out</vs-button>
        </div>
      </vs-sidebar>
    </div>
  </v-toolbar>
  </div>
</template>

<script>
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import Vue from 'vue'

Vue.use(Vuesax);

export default {
	name: 'Header',
  data:()=>({
    active:false,
  }),
  methods: {
		getImgUrl(img) {
			return require('../assets/' + img)
		},
    popUpMessage: function () {
        this.flashMessage.info({
        title: "즐겨찾기",
        message: "즐겨찾기는 ctrl + d를 눌러주세요.",
        icon: "https://image.flaticon.com/icons/svg/148/148839.svg"
        });
    }
	}
}
</script>

<style lang="stylus">
.header-sidebar
  display flex
  align-items center
  justify-content center
  flex-direction column
  width 100%
  h4
    display flex
    align-items center
    justify-content center
    width 100%
    > button
      margin-left 10px
.footer-sidebar
  display flex
  align-items center
  justify-content space-between
  width 100%
  > button
      border 0px solid rgba(0,0,0,0) !important
      border-left 1px solid rgba(0,0,0,.07) !important
      border-radius 0px !important
</style>
