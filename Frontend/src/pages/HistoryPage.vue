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
      
    </q-card-section>
  </q-card>
</template>
<script>
  import { defineComponent } from 'vue'
  import BreadCrums from 'components/layout/BreadCrums.vue';

  export default defineComponent({
    name: 'HistoryPage',
    components: {
      BreadCrums,
    },

    setup() {

      return {
        title: 'History Page',
        caption: 'Viw alls history record',
        breadcrumsLinks: [
        {
          label: 'Dashboard',
          color: 'indigo',
          icon: 'dashboard',
          link: '/Dashboard'
        },
        {
          label: 'History',
          color: 'indigo',
          icon: 'history_toggle_off',
          link: ''
        },
        ],

        
      }
    }
  })

</script>

