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

        <DataTable
          :columns="columns"
          :rows="rows"
          module="users"
        />
        
      </q-card-section>
    </q-card>
</template>
<script>
  import {defineComponent } from 'vue'
  import { date } from 'quasar'
  import BreadCrums from 'components/layout/BreadCrums.vue';
  import DataTable from 'components/DataTable.vue';
  import { httpClient } from '../../helpers/httpClient.js'
  import { capitalize } from '../../helpers/utils.js'

  
  export default defineComponent({
    name: 'UserProfile',
    components: {
      BreadCrums,
      DataTable
    },
    data () {
      return {
        columns: [],
        rows: []

      }
    },
    mounted () {

      this.columns = [
        { name: 'id', field: 'id', label: 'ID', align: 'center', sortable: true, },
        { name: 'username', field: 'username', label: 'Username',  align: 'center', sortable: true, },
        { name: 'fullname', field: 'fullname', label: 'Full Name',  align: 'center', sortable: true, },
        { name: 'email', field: 'email', label: 'Email', align: 'center', sortable: true, },
        { name: 'type_user', field: 'type_user', label: 'User Type',  align: 'center', sortable: true, },
        { name: 'last_login', field: 'last_login', label: 'Last Login', align: 'center', sortable: true, },
        { name: 'status', field: 'status', label: 'Status',  align: 'center', sortable: true, },
        { name: 'action', label: 'Actions', field: 'action', align: 'center', sortable: false, },
      ]
      
      httpClient.get('users/', {}, false, false, true).then((response) => {
        let rows = []
        response.results.forEach(function(record) {
          rows.push({
            'id': record.id,
            'username': record.username,
            'fullname': capitalize(record.first_name) + ' ' + capitalize(record.last_name),
            'email': record.email,
            'type_user': record.type_user.label,
            'last_login': date.formatDate(record.last_login, 'YYYY/MM/DD HH:mm:ss'),
            'status': record.status,
          })

        })
        this.rows = rows
      })

    },
    setup() {
  
      // let grid = false
  
      const breadcrumsLinks = [
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
        link: ''
      },
      ]
  
      return {
        title: 'Users List',
        caption: 'Manage your app users.',
        module: 'Users',
        breadcrumsLinks,
      }
    }
  })
</script>