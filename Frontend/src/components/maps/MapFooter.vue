<template>
  <LControlAttribution
  position="bottomright"
  :prefix="customAttributionPrefix"
  />
  <LControlScale position="bottomleft" :imperial="false" :metric="true" />
</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  import { 
    LControlAttribution,
    LControlScale
  } from '@vue-leaflet/vue-leaflet'

  export default defineComponent({
    name: 'MapFooter',
    components: {
      LControlAttribution,
      LControlScale
    },
    data() {
      return {
        customAttributionPrefix: '<b>By: Roger Zavarce</b>',
      }
    }
  });
</script>