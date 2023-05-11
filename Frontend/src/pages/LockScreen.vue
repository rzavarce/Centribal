<template>
  <q-layout class="bg-image" v-cloak>
    <q-page-container>
      <q-page class="flex flex-center">
        <q-card class="unlock_panel">
          <q-card-section>
            <q-avatar size="74px" class="absolute-center shadow-10">
              <img src="../assets/profile.svg">
            </q-avatar>
          </q-card-section>
          <q-card-section class="q-mt-md">
            <div class="text-h6 text-center">
              {{ userData.username }}
             
            </div>
            <q-form
          class="q-gutter-md"
          @submit="unlockPassword"
          >
            <q-input
              type="password"
              filled
              v-model="password"
              ref="passwordRef"
              hint="Insert your password"
              label="Password"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Fill the password please']"
            />
          <div>
              <q-chip v-if="unlockError" outline square color="red" text-color="white" icon="warning" label="Password is invalid." style="width: 100%;" />
            </div>
          <div class="row justify-center">
            <q-btn label="Send Reset Password" type="submit" color="primary" />
          </div> 
          </q-form>  
          </q-card-section>
          
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>

import {defineComponent} from 'vue'
import { LocalStorage } from 'quasar'
import CryptoJS from 'crypto-js'

export default defineComponent({
  name: 'LockScreen',
  data () {
      return {
        password: '',
        unlockError: false
      }
  },
  methods: {
    unlockPassword(){

      const passordStorage = CryptoJS.AES.decrypt(LocalStorage.getItem('lockPassword'), process.env.ENV_ENCRYPTION_KEY).toString(CryptoJS.enc.Utf8)

      if (this.password == passordStorage){

        LocalStorage.set('lockState', false)
        this.$router.go(-1)

      }else{
        this.unlockError = true
      }
    }
  },
  setup() {

    const userData = LocalStorage.getItem('userData')
    LocalStorage.set('lockState', true)
    return {
      userData
    }

  }

})
</script>

<style>


  [v-cloak] {
    display: none !important;
  }
  .unlock_panel {
    width: 20%;
  }
  @media screen and (max-width: 800px) {
    .unlock_panel {
      width: 40%;
    }
  }
  @media screen and (max-width: 600px) {
    .unlock_panel {
      width: 80%;
    }
  }

</style>