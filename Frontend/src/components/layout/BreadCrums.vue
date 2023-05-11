<template>
  <div class="row">
    <div class="col-xs-12 col-md-6">
      <span class="text-h6 text-blue-7">{{ title }}</span>
      <span class="text-caption" style="padding-left:5px"> {{ caption }}</span>
    </div>
    <div class="col-xs-12 col-md-6">
      <q-breadcrumbs class="breadcrums" active-color="blue-7">
        <template v-slot:separator>
          <q-icon
          size="1.2em"
          name="arrow_forward"
          color="blue-7"
          />
        </template>
        <q-breadcrumbs-el 
          v-for="item in breadcrumsLinks" 
          :key="item.label" 
          :to="item.link" 
          :label="item.label" 
          :icon="item.icon" 
        />
      </q-breadcrumbs>
    </div>
   </div> 
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'BreadCrums',
  props: {
    title: String,
    caption: String,
    breadcrumsLinks: Array
  }
});
</script>
