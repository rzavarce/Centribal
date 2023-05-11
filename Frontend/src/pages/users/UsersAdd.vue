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
      <div class="row">
        <div class="col-xs-12 col-sm-8 columns-forms">
          <q-form
          greedy
          class="q-gutter-md"
          @submit="onSubmitForm"
          @reset="onResetForm"
          @validation-error="onValidationError"
          >
          <q-input
            filled
            v-model="user.username"
            label="Username"
            hint="Insert username"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Username is required.']"
            />
          <q-input
            filled
            v-model="user.email"
            label="Email"
            hint="Insert your email"
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
            mask="####-##-##" 
            :rules="['']"
            :initDate="today"
            />
          <q-separator />
          <q-btn-group spread>
            <q-btn label="Save" type="submit" color="green-7" />
            <q-btn label="Reset" type="reset" color="blue-7" />
            <q-btn label="Cancel" type="button" color="red-7" @click="$router.replace('/Users/')"/>
          </q-btn-group>
          </q-form>
        </div>
        <div class="col-xs-12 col-sm-4 columns-history">
          <q-timeline color="secondary">
            <q-timeline-entry heading >
              <span class="text-h4">Timeline History</span>
              <q-separator />
            </q-timeline-entry>
            <q-timeline-entry
              v-for="(users_history, index) in users_history"
              :key="index"
              :title="users_history.title"
              :subtitle="users_history.date" 
              :color="users_history.color" 
              :icon="users_history.icon"
              :side="users_history.side"
              >
              <div>{{ users_history.description }}</div>
              <div class="text-caption"><b>By user:</b> {{ users_history.by_user }}</div>
            </q-timeline-entry>
          </q-timeline>
          <q-btn flat color="primary" label="See alls" to="/history" />
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>
<script>
  import { defineComponent } from 'vue'
  import { date } from 'quasar'
  import BreadCrums from 'components/layout/BreadCrums.vue';
  import DateInput from 'components/forms/DateInput.vue';
  import { httpClient } from '../../helpers/httpClient.js'
  import { emailValidation, scrollToError, resetModelForm, setHistoryData } from '../../helpers/utils.js'

  export default defineComponent({
    name: 'UserAdd',
    components: {
      BreadCrums,
      DateInput,
    },
    data () {
      return {
        user: {
          'username': 'rzavarce',
          'email': 'rogerzavarce@gmail.com',
          'first_name': 'Roger',
          'last_name': 'Zavarce',
          'type_user': 'Administrator',
          'address': 'Calle de la granja de San Ildelfonso, 38',
          'zip_code': '28051',
          'birth_date': '1979-07-26',
          'phone_number': '34601491522',
        },
        countries: [],
        user_types: [],
        users_history:{},
      }
    },
    methods: {

      async onSubmitForm() {

        httpClient.post('users/add/', this.user).then(() => {
          this.onResetForm()
        })
      
      },
      onResetForm () {
        resetModelForm(this.user)
      },
      isValidEmail (val) {
        return emailValidation(val)
      },
      onValidationError(ref) {
        scrollToError(ref)
      }
    },
    mounted () {
     
      httpClient.get('users/add/', {}, false, false, false).then((response) => {
        this.user_types = response.user_types_list
        this.users_history = setHistoryData(response.users_history, 'User', 'username')
      })

    },
    setup() {

      let today = new Date()
      today = date.subtractFromDate(today, { year: 18,})
      today = date.formatDate(today, 'YYYY/MM/DD')

      return {
        today,
        title: 'Users Add',
        caption: 'Register a new user.',
        breadcrumsLinks: [
        {
          label: 'Dashboard',
          color: 'indigo',
          icon: 'dashboard',
          link: '/Dashboard'
        },
        {
          label: 'Users',
          color: 'indigo',
          icon: 'group',
          link: '/Users'
        },
        {
          label: 'Add',
          color: 'indigo',
          icon: 'person_add',
          link: ''
        },
        ],

        
      }
    }
  })

</script>

