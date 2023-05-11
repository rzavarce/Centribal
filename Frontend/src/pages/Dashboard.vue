<template>
  <q-card bordered>
    <q-card-section>

      <p v-for="n in 15" :key="n">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit nihil praesentium molestias a adipisci, dolore vitae odit, quidem consequatur optio voluptates asperiores pariatur eos numquam rerum delectus commodi perferendis voluptate?
      </p>
    </q-card-section>
  </q-card>

</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'IndexPage',
    data (){
      return {
        search: ''
      }
    },
    setup () {
      return {
       
      }
    }

  });

</script>
