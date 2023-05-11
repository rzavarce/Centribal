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
          module="products"
        />
        
      </q-card-section>
    </q-card>
</template>
<script>
  import {defineComponent } from 'vue'
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
        { name: 'name', field: 'name', label: 'Name',  align: 'center', sortable: true, },
        { name: 'price', field: 'price', label: 'Price', align: 'center', sortable: true, },
        { name: 'tax', field: 'tax', label: 'Taxes',  align: 'center', sortable: true, },
        { name: 'stock', field: 'stock', label: 'Stock',  align: 'center', sortable: true, },
        { name: 'status', field: 'status', label: 'Status',  align: 'center', sortable: true, },
        { name: 'action', label: 'Actions', field: 'action', align: 'center', sortable: false, },
      ]
      
      httpClient.get('products/?get_all=true', {}, false, false, true).then((response) => {
        let rows = []
        response.forEach(function(record) {
          rows.push({
            'id': record.id,
            'reference': record.reference,
            'name': record.name,
            'price': record.price,
            'tax': record.tax,
            'stock': record.stock,
            'status': record.status,
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
        label: 'Products',
        color: 'indigo',
        icon: 'storefront',
        link: ''
      },
      ]
  
      return {
        title: 'Products List',
        caption: 'Manage your products.',
        module: 'Products',
        breadcrumsLinks,
      }
    }
  })
</script>