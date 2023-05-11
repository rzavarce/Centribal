<template>
  <q-card bordered>
    <q-card-section>
      <BreadCrums
        :title="title"
        :caption="caption"
        :breadcrumsLinks="breadcrumsLinks"
        />
    </q-card-section>
    <q-separator />
    <q-card-section>
      <q-tabs
        v-model="tab"
        inline-label
        align="justify"
        class="bg-primary text-white shadow-2"
        style="border-radius: 5px 5px 0px 0px;"
      >
        <q-tab name="profile" icon="person_pin" label="Profile" />
        <q-tab name="settings" icon="settings" label="Settings" />
        <q-tab name="password" icon="password" label="Password" />
        
      </q-tabs>
      <q-tab-panels
          v-model="tab"
          animated
          transition-prev="jump-up"
          transition-next="jump-up"
          style="border: 1px solid black; border-radius: 0px 0px 5px 5px;"
        >
          <q-tab-panel name="profile" align="center">
            <div class="text-h6 q-mb-md" style="">
                Profile Change
              </div>

            <div style="max-width: 600px; margin-top: 20px;">
              <q-form
          greedy
          class="q-gutter-md"
          @submit="onSettingsForm"
          @reset="onResetForm"
          @validation-error="onValidationError"
          >
          <q-input
            filled
            disable
            v-model="user.username"
            label="Username"
            hint="Username registered"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Username is required.']"
            />
          <q-input
            filled
            disable
            v-model="user.email"
            label="Email"
            hint="User email saved"
            lazy-rules
            :rules="[ isValidEmail ]"
            />
          <q-input
            filled
            v-model="user.first_name"
            label="First Name"
            hint="Insert first name"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'First Name is required.']"
            />
          <q-input
            filled
            v-model="user.last_name"
            label="Last Name"
            hint="Insert last name"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Last Name is required.']"
            />
          <q-select
            filled
            v-model="user.type_user"
            :options="user_types"
            emit-value
            map-options
            label="User Type" 
            hint="Select user type"
            :rules="[ val => val || 'You must make a selection.']"
            />
          <q-select 
            filled 
            v-model="user.country" 
            :options="countries"
            option-value="id"
            option-label="name"
            option-disable="inactive"
            emit-value
            map-options 
            label="Country" 
            hint="Select user country"
            :rules="[ val => val || 'You must make a selection.']" 
            />
          <q-input
            filled
            v-model="user.city"
            label="City"
            hint="Insert user city"
            />
          <q-input
            filled
            v-model="user.address"
            label="Address"
            hint="Insert user address"
            />
          <q-input
            filled
            type="number"
            v-model="user.zip_code"
            label="Zip Code"
            hint="Insert user zip code"
            min="1000" 
            max="99999"
            />
          <q-input
            filled
            v-model="user.phone_number"
            label="Phone Number"
            hint="Only numbers are permited"
            mask="+## ### ### ###"
            />
          <DateInput 
            label="Birthdate" 
            hint="Birthdate user" 
            v-model="user.birth_date"
            mask="date" 
            :rules="['']"
            :initDate="today"
            />
          <FileInput 
            label="Avatar" 
            hint="Update a picture avatar" 
            v-model="user.avatar" 
            />
          <q-separator />
          <q-btn-group spread>
            <q-btn label="Save" type="submit" color="green-7" />
            <q-btn label="Reset" type="reset" color="blue-7" />
            <q-btn label="Cancel" type="button" color="red-7"  @click="$router.replace('/Dashboard')"/>
          </q-btn-group>
          </q-form>
            </div>
          </q-tab-panel>

          <q-tab-panel name="settings" align="center">
            <div class="text-h6 q-mb-md" style="">
                App Setting
              </div>

            <div style="max-width: 600px; margin-top: 20px;">
            <q-form
              greedy
              class="q-gutter-md"
              @submit="onSubmitForm"
              @reset="onResetForm"
              @validation-error="onValidationError"
              >

              <q-toggle v-model="settings.location" label="Locations" />


            </q-form>
            </div>
          </q-tab-panel>

          <q-tab-panel name="password" align="center">
              <div class="text-h6 q-mb-md" style="">
                Password Change
              </div>

            <div style="max-width: 600px; margin-top: 20px;">
            <q-form
            greedy
          class="q-gutter-md"
          @submit="onPasswordChange"
          >
          <q-input
          type="password"
          filled
          v-model="password_change.current_password"
          label="Current Password"
          hint="Insert your current Password"
          lazy-rules
          :rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.']"
          />

          <q-input
          type="password"
          filled
          v-model="password_change.new_password"
          label="New Password"
          hint="Insert your new Password"
          lazy-rules
          :rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.']"
          />

          <q-input
          type="password"
          filled
          v-model="password_change.confirm_password"
          label="Confirm Password"
          hint="Confirm your new Password"
          lazy-rules
          :rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.', 
           val => val && val==password_change.new_password || 'Passwords not match']"
          />

          <q-input
          filled
          v-model="user"
          lazy-rules
          style="display:none;"
          />
          
          <q-separator />
          <q-btn-group spread>
            <q-btn label="Save" type="submit" color="green-7" />
            <q-btn label="Reset" type="reset" color="blue-7" />
            <q-btn label="Cancel" type="button" color="red-7" @click="tab='profile'"/>
          </q-btn-group>
        </q-form> 
          </div>
          </q-tab-panel>
        </q-tab-panels>
      
    </q-card-section>
  </q-card>
</template>
<script>
  import { defineComponent, ref } from 'vue'
  import { LocalStorage } from 'quasar'
  import { date } from 'quasar'
  import BreadCrums from 'components/layout/BreadCrums.vue'
  import FileInput from 'components/forms/FileInput.vue'
  import DateInput from 'components/forms/DateInput.vue'
  import { httpClient } from '../helpers/httpClient.js'
  import { emailValidation, scrollToError, resetModelForm, } from '../helpers/utils.js'

  export default defineComponent({
    name: 'ProfilePage',
    components: {
      BreadCrums,
      DateInput,
      FileInput,
    },
    data () {
      return {
        user: {},
        settings: {
          'location': true,
        },
        password_change: {}, 
        countries: [],
        user_types: [],
      }
    },
    methods: {

      async onSubmitForm() {
        
        const pk = this.userData.id

        let data = this.user

        data.type_user = typeof(data.type_user) === 'object' ? data.type_user.value : data.type_user
        data.country = typeof(data.country) === 'object' ? data.country.id : data.country
        httpClient.put('users/edit/' + pk + '/', data).then((response) => {
          console.log(response)
        })
      
      },
      onResetForm () {
        resetModelForm(this.user)
      },
      isValidEmail (val) {
        return emailValidation(val)
      },
      onValidationError(element) {
        scrollToError(element)
      },
      onPasswordChange() {

        const payload = {
          'current_password': this.password_change.current_password,
          'new_password': this.password_change.new_password,
          'user':  this.userData.id
        }
        console.log(payload)
        
        httpClient.post('users/change-password/', payload).then((response) => {
          console.log(response)
        })
        

      },
      onSettingsForm() {
        
        console.log(this.settings)

      },
    },
    mounted () {

      const pk = this.userData.id
     
      httpClient.get('users/edit/' + pk + '/', {}, false, false, false).then((response) => {
        console.log(response.user_data)
        this.user = response.user_data[0]
        this.countries = response.countries_list
        this.user_types = response.user_types_list
      })

    },
    setup() {
      const userData = LocalStorage.getItem('userData')
      let today = new Date()
      today = date.subtractFromDate(today, { year: 18,})
      today = date.formatDate(today, 'YYYY/MM/DD')

      return {
        today,
        userData,
        title: 'Profile',
        caption: 'Manage your profile.',
        tab: ref('profile'),
        breadcrumsLinks: [
        {
          label: 'Dashboard',
          color: 'indigo',
          icon: 'dashboard',
          link: '/Dashboard'
        },
        {
          label: 'Profile',
          color: 'indigo',
          icon: 'badge',
          link: ''
        },
        ],

        
      }
    }
  })

</script>