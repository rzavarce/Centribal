import { defineStore } from 'pinia';
import { LocalStorage } from 'quasar'
import { Cookies } from 'quasar'
import { httpClient } from '../helpers/httpClient.js'


import CryptoJS from 'crypto-js';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    recoveryPasswordSended: false,
    passwordResetError: false,
    lockPassword: '',
    lockState: false,
    userData: {},
    userError: {}
  }),

  actions: {
    async login(email, password, remember) {  

      httpClient.post('login/', {email, password}, true, false, true).then((response) => {
        if (response.token){

          LocalStorage.set('isAuthenticated', true)
          LocalStorage.set('userData', response.user)
          LocalStorage.set('access_token', response.token)
          LocalStorage.set('lockState', false)
          LocalStorage.set('lockPassword', CryptoJS.AES.encrypt(password, process.env.ENV_ENCRYPTION_KEY).toString())

          if(remember){
            const userEncrypt = CryptoJS.AES.encrypt(email, process.env.ENV_ENCRYPTION_KEY).toString()
            Cookies.set('centribaluser', userEncrypt)
            const passwordEncrypt = CryptoJS.AES.encrypt(password, process.env.ENV_ENCRYPTION_KEY).toString()
            Cookies.set('centribalpassword', passwordEncrypt)
          }else{
            Cookies.remove('centribaluser')
            Cookies.remove('centribalpassword')
          }

          this.router.push({ name: 'dashboard' })

        }

      })

    },
    async logout() {

      httpClient.post('logout/', {}, false, false, true)

      this.userData = {};
      localStorage.removeItem('isAuthenticated')
      localStorage.removeItem('userData')
      this.router.push({ name: 'login' })
    },

    async passwordRecovery(email) {

      console.log(email)

      httpClient.post('users/password_reset/', {email}).then((response) => {

        console.log(response)
      

      })

    },

    async passwordReset(password, passwordConfirmation, user) {

      if (password == passwordConfirmation) {
         httpClient.post('users/password_reset/confirm/', {password, user}).then((response) => {
          console.log(response)
        })
      }


    },

  }
});
