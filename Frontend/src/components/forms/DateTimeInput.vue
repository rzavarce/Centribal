<template>
  <div>
    <q-input filled :label="label" v-model="datetime" :mask="mask" :rules="rules">
      <template v-slot:prepend>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-date 
            v-model="datetime" 
            mask="YYYY-MM-DD HH:mm"
            :options="datetime => datetime <= initDate"
            :default-year-month="initDate.substr(0, 7)"
            >
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
          </q-popup-proxy>
        </q-icon>
      </template>

      <template v-slot:append>
        <q-icon name="access_time" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-time v-model="datetime" mask="YYYY-MM-DD HH:mm" format24h>
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-time>
          </q-popup-proxy>
        </q-icon>
      </template>

      <template v-slot:hint>
        {{ hint }}
      </template>
    </q-input>
  </div>
</template>

<script lang="ts">
  import { defineComponent, } from 'vue';

  export default defineComponent({
    name: 'DateInput',
    props: ['label', 'hint', 'mask', 'rules', 'initDate'],
    data() {
      return {
        datetime: '',
      };
    },

  });
</script> 
