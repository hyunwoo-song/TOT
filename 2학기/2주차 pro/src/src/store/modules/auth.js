import api from "../../api/imgur";
import qs from "qs";
import { router } from "../../main";

const state = {
  token: 'bb0ca67e10a737baf905f8263e3c99ade9d8743b'
};

const getters = {
  isLoggedIn: state => !!state.token
};

const actions = {
};

const mutations = {
  setToken: (state, token) => {
    state.token = token;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
