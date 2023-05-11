<template>
  <q-layout view="hHh Lpr fFf">
    <q-header elevated>
      <q-toolbar>
        <div class="logo_navbar">
          <img src="https://i.ibb.co/pLm1w9H/Logo-Developper-Dark.png" style="margin:10px 0px 0px 0px; height: 40px;">
        </div>
        <q-btn
          flat
          dense
          round
          @click="drawer = !drawer"
          icon="menu"
          aria-label="Menu"
          >
          <q-tooltip>All Menu Toggle</q-tooltip>
        </q-btn>
        <q-toggle
          color="blue"
          size='xs'
          checked-icon="check"
          unchecked-icon="clear"
          v-model="miniActive"
          @click="drawerClick"
          class="gt-xs"
          >
          <q-tooltip>Minimenu toggle</q-tooltip>
        </q-toggle>
        <q-space/>
        <q-btn 
          round 
          dense 
          flat 
          color="white" 
          :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
          @click="$q.fullscreen.toggle()" 
          >
          <q-tooltip>{{ $q.fullscreen.isActive ? 'Exit Fullscreen' : 'Toggle Fullscreen' }}</q-tooltip>
        </q-btn>
        <q-btn
          flat
          dense
          round
          :icon="btnIcon"
          aria-label="Dark Mode"
          @click="toggleDarkMode"
          >
          <q-tooltip>{{ this.btnIcon == 'wb_sunny' ? 'Dark Mode' : 'Exit Dark Mode' }}</q-tooltip>
        </q-btn>
        <MessagesMenu />
        <ProfileMenu />
      </q-toolbar>
    </q-header>
    <q-drawer
      v-model="drawer"
      show-if-above
      :mini="!drawer || miniState"
      @mouseover="miniState = false"
      @mouseout="hideMiniSite"
      :width="300"
      :breakpoint="500"
      bordered
      content-class="bg-primary text-white"
      >
      <PrincipalMenu />
    </q-drawer>
    <q-page-container>
      <q-page padding>

        <router-view v-slot="{ Component }">
          <transition
            appear
            enter-active-class="animated slideInLeft"
            leave-active-class="animated slideOutRight"
            :duration='500'
          >
            <component :is="Component" />
          </transition>
        </router-view>

        <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[5, 5]">
          <q-btn round icon="keyboard_arrow_up" color="primary" />
        </q-page-scroller>
      </q-page>
    </q-page-container>
    <FooterBar />
  </q-layout>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';
  import { Dark } from 'quasar'
  import PrincipalMenu from 'components/layout/PrincipalMenu.vue';
  import MessagesMenu from 'components/layout/MessagesMenu.vue';
  import ProfileMenu from 'components/layout/ProfileMenu.vue';
  import FooterBar from 'components/layout/FooterBar.vue';
  
  export default defineComponent({
    name: 'MainLayout',
    data () {
      return {
        btnIcon:'wb_sunny',
        drawer: false,
      //miniActive: true,
      //miniState: false,
        miniActive: false,
        miniState: false,
      }
    },
  
    components: {
      PrincipalMenu,
      MessagesMenu,
      ProfileMenu,
      FooterBar,
    },
  
    methods: {
  
      drawerClick () {
        this.miniState = !this.miniState
      },
  
      toggleDarkMode: function () {
        this.btnIcon = this.btnIcon == 'wb_sunny' ? 'nights_stay' : 'wb_sunny'
        Dark.toggle();
      },
  
      showMiniSite (e) {
        console.log(this.miniActive)
        if (this.miniActive) {
          this.miniState = true
          e.stopPropagation()
        }
      },
  
      hideMiniSite (e) {
        if (this.miniActive) {
          this.miniState = true
          e.stopPropagation()
        }
      },
  
    },
  
  })
</script>
