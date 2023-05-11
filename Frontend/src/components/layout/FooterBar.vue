<template>
  <q-footer class="bg-black-8 text-white">
    <div class="row" style="padding: 10px;">
      <span class="text-body5 text-white text-weight-bold" style="padding-top: 5px;">
        © {{ new Date().getFullYear() }} 
        <a href="https://thepubcrawlcompany.com/" class="text-red text-bold" target="_blank">PubCrawlCompany</a>. All rights reserved.
      </span>
      <q-space></q-space>
      <div class="gt-xs">
        <q-btn 
        round 
        dense 
        flat 
        color="red"
        type="a" 
        title="Linkedin" 
        href="https://www.linkedin.com/in/rogerzavarce/"
        target="_blank"
        >
        <i class="fa fa-heart fa-2x fa-beat"></i>
      </q-btn>
      <q-btn 
      icon="fab fa-github" 
      flat 
      dense 
      color="white-8"
      type="a" 
      title="Github" 
      href="https://github.com/"
      target="_blank"
      />
      <q-btn 
      icon="fab fa-facebook" 
      flat 
      dense 
      color="white-8"
      type="a" 
      title="Facebook" 
      href="https://facebook/"
      target="_blank"
      />
      <q-btn 
      icon="fab fa-twitter" 
      flat 
      dense 
      color="white-8"
      type="a" 
      title="Twitter" 
      href="https://twitter/"
      target="_blank"
      />
      <q-btn 
      icon="fab fa-instagram" 
      flat 
      dense 
      color="white-8"
      type="a" 
      title="Instagram" 
      href="https://instagram/"
      target="_blank"
      />
    </div>
  </div>
</q-footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'FooterBar',

});
</script>
