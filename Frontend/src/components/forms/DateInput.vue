<template>
  <div>
    <q-input filled :label="label" v-model="date" :mask="mask" :rules="rules">
      <template v-slot:append>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-date 
            v-model="date"
            mask="YYYY-MM-DD" 
            :options="date => date <= initDate"
            :default-year-month="initDate.substr(0, 7)"
            >
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
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
    methods: {
    },
    data() {
      return {
        date: '',
      };
    },

  });
</script> 