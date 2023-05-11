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
          module="orders"
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
        { name: 'reference', field: 'reference', label: 'Reference',  align: 'center', sortable: true, },
        { name: 'price_total', field: 'price_total', label: 'Total Amount',  align: 'center', sortable: true, },
        { name: 'price_total_tax', field: 'price_total_tax', label: 'Total With Tax', align: 'center', sortable: true, },
        { name: 'created_date', field: 'created_date', label: 'Created Date', align: 'center', sortable: true, },
        { name: 'action', label: 'Actions', field: 'action', align: 'center', sortable: false, },
      ]
      
      httpClient.get('orders/?get_all=true', {}, false, false, true).then((response) => {
        let rows = []
        response.forEach(function(record) {
          rows.push({
            'id': record.id,
            'reference': record.reference,
            'price_total': record.price_total,
            'price_total_tax': record.price_total_tax,
            'created_date': date.formatDate(record.created_date, 'YYYY/MM/DD HH:mm:ss'),
          })

        })
        this.rows = rows
      })

    },
    setup() {
      const breadcrumsLinks = [
      {
        label: 'Dashboard',
        color: 'indigo',
        icon: 'dashboard',
        link: '/Dashboard'
      },
      {
        label: 'Orders',
        color: 'indigo',
        icon: 'list_alt',
        link: ''
      },
      ]
  
      return {
        title: 'Orders List',
        caption: 'Manage your orders here.',
        module: 'Orders',
        breadcrumsLinks,
      }
    }
  })
</script>