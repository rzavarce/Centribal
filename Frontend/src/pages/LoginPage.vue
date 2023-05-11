<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex bg-image flex-center">
        <q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}">
          <q-card-section>
            <q-avatar size="103px" class="absolute-center shadow-10">
              <img src="../assets/profile.svg">
            </q-avatar>
          </q-card-section>
          <q-card-section>
            <div class="text-center q-pt-lg">
              <div class="col text-h6 ellipsis">
                Log in
              </div>
            </div>
          </q-card-section>
          <q-card-section v-if="login_form_display">
            <q-form
              greedy
              class="q-gutter-md"
              @submit="onSubmitLogin"
              @reset="onResetForm"
            >
            <q-input
              filled
              v-model="email"
              label="Email"
              hint="Insert your email"
              lazy-rules
              :rules="[ isValidEmail ]"
            />

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

            <div align="center">
            <q-checkbox 
            v-model="remember" 
            label="Remember" 
            style="margin-right: 15px;"
            />

            <q-btn flat color="primary" label="Forgot your password?" @click="toggleForms"  />
            </div>
          <q-btn-group spread>
            <q-btn label="Login" type="submit" color="green-7" />
            <q-btn label="Reset" type="reset" color="red-7" />
          </q-btn-group>

          </q-form>
          

        </q-card-section>

        <q-card-section v-if="forgot_password_display">
          <q-form
              class="q-gutter-md"
              @submit="onSubmitRecovery"
            >
          <q-input
              filled
              v-model="recovery"
              label="Email"
              hint="Insert your email"
              lazy-rules
              :rules="[ isValidEmail ]"
            />

          <div class="row justify-center">
            <q-btn label="Send Recovery Password" type="submit" color="primary" />
          </div>
        </q-form> 
        <div class="row justify-center" style="margin:20px;">  
          <q-btn flat color="primary" label="Back to Login"  @click="toggleForms" />
        </div>         
      </q-card-section>
    </q-card>
  </q-page>
</q-page-container>
</q-layout>
</template>

<script>
  import {defineComponent } from 'vue'
  import { Cookies } from 'quasar'
  import CryptoJS from 'crypto-js'
  import { useAuthStore } from 'stores/auth'
  import { emailValidation, } from '../helpers/utils.js'

  export default defineComponent({
    data () {
      return {
        email: this.getCookie('centribaluser'),
        recovery: 'rogerzavarce@gmail.com',
        password: this.getCookie('centribalpassword'),
        remember: Cookies.has('centribaluser') && Cookies.has('centribalpassword'),
        login_form_display: true,
        forgot_password_display: false,
      }
    },
    methods: {

      async onSubmitLogin() {

        await this.authStore.login(this.email, this.password, this.remember)

      },

      async onSubmitRecovery() {

        await this.authStore.passwordRecovery(this.recovery)
      
      },

      onResetForm () {
        this.email = ''
        this.password = ''
        this.remember = false
      },

      isValidEmail (val) {
        return emailValidation(val)
      },

      toggleForms () {
        this.forgot_password_display = !this.forgot_password_display
        this.login_form_display = !this.login_form_display
      },

      getCookie (name) {
        if(Cookies.has(name)){
          const cookie = Cookies.get(name)
          const decrypt = CryptoJS.AES.decrypt(cookie, process.env.ENV_ENCRYPTION_KEY).toString(CryptoJS.enc.Utf8)
          return decrypt
        }
        return null
      }

    },

    setup() {
      const authStore = useAuthStore()

      return { 
        authStore,
      }
    }

    })
  </script>

  <style>
  </style>