<template>
  <LControl
  class="leaflet-control leaflet-demo-control"
  position="topleft"
  >
    <q-btn
    @click="FullScreenToggle"
    :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
    class="fullscreen_button"
    />
  </LControl>
</template>

<script lang="ts">
  import { defineComponent } from 'vue'

  import useQuasar from 'quasar/src/composables/use-quasar.js';

  import { 
    LControl,
  } from '@vue-leaflet/vue-leaflet'

  export default defineComponent({
    name: 'FullScreenButton',
    components: {
      LControl
    },
    setup() {
      const $q = useQuasar()
      return {
        FullScreenToggle (e) {
          const target = e.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode
          $q.fullscreen.toggle(target)
        }
      }
    }
  });
</script>