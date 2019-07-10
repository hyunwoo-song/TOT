<template>
  <v-app>
    <!-- header -->
    <Header></Header>

    <!-- content -->
    <v-content id="content">
      <router-view/>
    </v-content>

    <!-- footer -->
    <v-footer height="auto">
      <Footer></Footer>

    </v-footer>

    <!-- go-top -->
    <go-top bg-color="#3f51b5"></go-top>

    <!-- Flash message -->
    <FlashMessage></FlashMessage>
  </v-app>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'

import GoTop from '@inotom/vue-go-top';
import store from './store';

export default {
	name: 'App',
	store,
  created() {
    // 브라우저 최적화
    let browser = navigator.userAgent.toLowerCase();

    if(browser.indexOf("chrome") > 0) {
      if(browser.indexOf("opr") > 0 || browser.indexOf("edge") > 0){
        this.flashMessage.info({
          title: '알림',
          message:'chrome에 최적화된 사이트입니다',
          icon:'https://image.flaticon.com/icons/svg/272/272340.svg'
        });
      }
    } else {
      this.flashMessage.info({
        title: '알림',
        message: 'chrome에 최적화된 사이트입니다',
        icon: 'https://image.flaticon.com/icons/svg/272/272340.svg'
      });
    };
  },
  components: {  
    GoTop,
    Header,
    Footer

  }
}

</script>
