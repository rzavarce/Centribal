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
    name: 'OthersPage',
    components: {
      BreadCrums,
    },

    setup() {

      return {
        title: 'Template page',
        caption: ' Admin your template.',
        breadcrumsLinks: [
        {
          label: 'Dashboard',
          color: 'indigo',
          icon: 'dashboard',
          link: '/Dashboard'
        },
        {
          label: 'Others',
          color: 'indigo',
          icon: 'dynamic_feed',
          link: ''
        },
        ],

        
      }
    }
  })

</script>
