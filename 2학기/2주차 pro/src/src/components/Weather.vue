<template>
<!-- 위치 기반 날씨 정보-->
    <!-- <div>
      <div id="weather">
        <img v-bind:src="icon"> {{overcast}}
        <br>
         <span class="temperature">{{currentTemp}}°</span><br>
         <span id="temp-values">Min {{minTemp}}° <br> Max {{maxTemp}}°</span>
     </div>
     <div id="info">
       <img class="icon" src="./images/sunrise.svg"> {{sunrise}}
       <img class="icon" src="./images/sunset.svg"> {{sunset}}
       <img class="icon" src="./images/humidity.svg"> {{humidity}}
       <img class="icon" src="./images/pressure.svg"> {{pressure}}
       <img class="icon" src="./images/wind.svg"> {{wind}}
     </div>
    </div> -->
    <div >
<a class="weatherwidget-io" href="https://forecast7.com/en/36d12128d34/gumi-si/" data-label_1="GUMI" data-label_2="WEATHER" data-theme="hexellence" >GUMI WEATHER</a>
</div>

</template>


<script>
import axios from 'axios';
const API = 'http://api.openweathermap.org/data/2.5/weather?units=metric';
const KEY = '&APPID=57f5d25e271adfbd7e7ddefe35cc0669';

  export default{
  name: 'Weather',

    data(){
      return{
        currentTemp: '',
        minTemp: '',
        maxTemp:'',
        sunrise: '',
        sunset: '',
        pressure: '',
        humidity: '',
        wind: '',
        overcast: '',
        icon: '',
        location: ''
      }

    },
  methods: {
    getWeather(url) {
      axios
        .get(url)
        .then(response => {
          this.currentTemp = response.data.main.temp;
          this.minTemp = response.data.main.temp_min;
          this.maxTemp = response.data.main.temp_max;
          this.pressure = response.data.main.pressure;
          this.humidity = response.data.main.humidity + '%';
          this.wind = response.data.wind.speed + 'm/s';
          this.overcast = response.data.weather[0].description;
          this.icon ="http://openweathermap.org/img/w/" + response.data.weather[0].icon + ".png";
          this.sunrise = new Date(response.data.sys.sunrise*1000).toLocaleTimeString("en-GB").slice(0,5);
          this.sunset = new Date(response.data.sys.sunset*1000).toLocaleTimeString("en-GB").slice(0,5);
          console.log(this.icon);
      })
      .catch(error => {
        console.log(error);
      });
    },
    geolocation() {
      navigator.geolocation.getCurrentPosition(this.buildUrl, this.geoError);
    },
    buildUrl(position) {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;

      this.getWeather(API + '&lat=' + lat + '&lon=' + lon + KEY);
    },
    geoError(error) {
      this.getWeather(API + '&lat=0&lon=0' + KEY);
    }
  },
  mounted() {
    this.geolocation();
  },
}
//   methods: {
//     getWeather() {
//       let url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=57f5d25e271adfbd7e7ddefe35cc0669";
//       axios.get(url)
//         .then(response => {
//           console.log(response.data);
//           this.results = response.data;
//           // this.currentTemp = response.data.main.temp;
//           // this.minTemp = response.data.main.temp_min;
//           // this.maxTemp = response.data.main.temp_max;
//           // this.pressure = response.data.main.pressure;
//           // this.humidity = response.data.main.humidity + '%';
//           // this.wind = response.data.wind.speed + 'm/s';
//           // this.overcast = response.data.weather[0].description;
//           // this.icon = "images/" + response.data.weather[0].icon.slice(0, 2) + ".svg";
//           // this.sunrise = new Date(response.data.sys.sunrise*1000).toLocaleTimeString("en-GB").slice(0,4);
//           // this.sunset = new Date(response.data.sys.sunset*1000).toLocaleTimeString("en-GB").slice(0,4);
//       })
//       .catch(error => {
//         console.log(error);
//       });
//     },
//   },
//   mounted() {
//     this.getWeather();
//   },
// }

</script>
<style>


#weather {
padding: 15px;
vertical-align: middle;
}

.temperature {
font-family: 'Vast Shadow', cursive;
font-size: 40px;
vertical-align: top;
position: absolute;
left: 80px;
}

#temp-values {
text-align: right;
text-justify: distribute;
display: block;
position: relative;
top: -60px;
}

#info {
padding-left: 20px;
position: relative;
top: -20px;
}

.icon {
position: inherit;
top: 2px;
padding-left: 8px;
}

</style>
