<template>
    <v-flex class="fluid" flat tile>
      <v-card-title class="indigo white--text justify-center">
        <strong class="subheading">&copy;2019 - SSAFY #GUMI #3 김호준</strong>
      </v-card-title>
      <Weather></Weather>
      <v-card-actions class="grey darken-3 white--text justify-center">
        week1 project — <strong>multicampus</strong>

      </v-card-actions>
    </v-flex>
</template>

<script>

import Weather from './Weather'

  export default{
    name : 'Footer',
    data () {
      return {
        results: {}
      }
  },

        components: {
          Weather
        }
  }

</script>
<style>
</style>
