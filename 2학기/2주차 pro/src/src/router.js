import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import PostPage from './views/PostPage.vue'
import PortfolioPage from './views/PortfolioPage.vue'
import LoginPage from './views/LoginPage.vue'
import PortfolioDetailPage from './views/PortfolioDetailPage.vue'
import PortfolioWriterPage from './views/PortfolioWriterPage.vue'
import YoutubePage from './views/YoutubePage.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
		{
			path: '/',
			name: 'home',
			component: HomePage
		},
		{
			path: '/post',
			name: 'post',
			component: PostPage
		},
		{
			path: '/portfolio',
			name: 'portfolio',
			component: PortfolioPage
		},
		{
			path: '/login',
			name: 'login',
			component: LoginPage
		},
    {
			path: '/portfolioDetail/:portfolioInfo',
			name: 'portfolioDetail',
			component: PortfolioDetailPage
		},
    {
      path: '/portfolioWriter',
      name: 'portfolioWriter',
      component: PortfolioWriterPage
    },
    {
      path: '/youtube',
      name: 'youtube',
      component: YoutubePage
    }
  ]
})
