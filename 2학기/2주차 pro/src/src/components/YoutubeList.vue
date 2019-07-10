<template>
  <v-layout mt-5 wrap>
    <v-flex v-for="i in youtubeList.length > limits ? limits : youtubeList.length" xs12 sm6 md3>
      <Youtube  :url="youtubeList[i-1].snippet.resourceId.videoId | getUrl" class="ma-3"></Youtube>
    </v-flex>
  </v-layout>
</template>

<script>
import Youtube from '@/components/Youtube'

export default{
  name: 'youtubeList',
  props: {
    limits: {type: Number, default: 4},
  },
  data(){
    return {
      youtubeList : []
    }
  },
  methods : {
    loadClient(){
      gapi.client.setApiKey("AIzaSyCq0Rslj8hl_vTHskY0-TkjyvASnso0ptU");
      return gapi.client.load("https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest")
          .then(function() { console.log("GAPI client loaded for API"); },
                function(err) { console.error("Error loading GAPI client for API", err); });
    },
    execute(){
      return gapi.client.youtube.playlistItems.list({
          "part": "snippet,contentDetails",
          "maxResults": 25,
          "playlistId": "PL94Czg4DS-dUjVkFmIxffg3x5YcM1R4l1"
        })
        .then(response => {
          this.youtubeList = response.result.items;
        },
        function(err) { console.error("Execute error", err); });
    }
  },
  created(){
    gapi.load("client:auth2", () => {
      gapi.auth2.init({client_id: "664802643968-2af371ouac4ne9es6pok2fhjmpnounqq.apps.googleusercontent.com"});
      this.loadClient().then(this.execute);
    });
  },
  filters : {
    getUrl(url){
      return 'https://www.youtube.com/embed/' + url ;
    }
  },
  components : {
    Youtube
  }
}
</script>
