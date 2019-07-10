<template>
  <div v-if="!showLoading" class="dropper">
    <input multiple accept="image/*" type="file" @change="uploadImages($event.target.files)">
    <span>Drag files here!!!!</span>
  </div>
  <div v-else class="centered">
    <ImgSpinner/>
    <div class="wait">Please Wait</div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import ImgSpinner from "./ImgSpinner";
export default {
  name: "ImgUpload",
  components: {
    ImgSpinner
  },
  computed: mapGetters(["showLoading"]),
  methods: mapActions(["uploadImages"])
};
</script>

<style scoped>
.dropper {
  height: 30vh;
  border: 2px dashed black;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.dropper:hover {
  background-color: #eee;
  cursor: pointer;
}

.centered {
  margin: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.wait {
  display: block;
  margin: 10px;
}

input {
  width: 100%;
  height: 30vh;
  position: absolute;
  opacity: 0;
}
</style>
