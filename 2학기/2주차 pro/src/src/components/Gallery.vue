<template>
  <div v-if="isLoggedIn" class="image-container">
    <img v-for="image in allImages" :key="image.link" :src="image.link">
  </div>
  <h2 v-else>Please Log-In</h2>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Gallery",
  computed: mapGetters(["allImages", "isLoggedIn"]),
  created() {
    this.fetchImages();
  },
  methods: mapActions(["fetchImages"])
};
</script>

<style scoped>
.image-container {
  column-count: 3;
  column-gap: 0;
}

img {
  max-width: 100%;
  padding: 5px;
}
</style>
