<template>
<q-file filled bottom-slots v-model="model" :label="label" counter use-chips>
        <template v-slot:prepend>
          <q-icon name="cloud_upload" @click.stop.prevent />
        </template>
        <template v-slot:append>
          <q-icon name="close" @click.stop.prevent="model = null" class="cursor-pointer" />
        </template>

        <template v-slot:hint>
          {{ hint }}
        </template>
      </q-file>
</template>

<script lang="ts">
  import { defineComponent, ref } from 'vue';

  export default defineComponent({
    name: 'FileInput',
    props: ['label', 'hint'],
    data() {
      return {
        model: ref(null),
      };
    },

  });
</script> 





