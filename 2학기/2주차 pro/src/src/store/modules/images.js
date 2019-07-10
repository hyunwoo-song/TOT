import api from "../../api/imgur";
import { router } from "../../main";

const state = {
  images: [],
  loading: false
};
const getters = {
  allImages: state => state.images,
  showLoading: state => state.loading
};

const actions = {
  async fetchImages({ commit, rootState }) {
    const { token } = rootState.auth;
    const response = await api.fetchImages(token);
    commit("setImages", response.data.data);
  },

  async uploadImages({ commit, rootState }, images) {
    const { token } = rootState.auth;
    commit("setLoading", true);
    await api.uploadImages(images, token);
    commit("setLoading", false);
  }
};

const mutations = {
  setImages: (state, images) => {
    state.images = images;
  },
  setLoading: (state, isLoading) => {
    state.loading = isLoading;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
