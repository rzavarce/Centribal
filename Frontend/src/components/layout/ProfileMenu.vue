<template>
  <q-btn round flat title="User Profile">
    <q-avatar size="26px">
      <img src="../../assets/profile.svg">
    </q-avatar>
    <q-menu>
      <q-card>
        <q-item style="height: 100px;">
          <q-item-section avatar >
            <q-avatar>
              <img src="../../assets/profile.svg">
            </q-avatar>
          </q-item-section>

          <q-item-section>
            <q-item-label>{{ userData.username }}</q-item-label>
            <q-item-label caption>
              {{ userData.email }}
            </q-item-label>
          </q-item-section>
        </q-item>

        <q-separator inset />

        <q-card-section>
          <q-item>
            <q-item-label caption>
              <b>Last Login: </b>{{ userData.last_login }}
            </q-item-label>
          </q-item>
          <div class="text-h10">Activity</div>
          <q-item>
            <q-item-section class="text-h12">
              Settings
            </q-item-section>

            <q-item-section>
              <q-badge rounded color="primary" label="999+" style="max-width: 40px; margin-left: 40px;" />
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section class="text-h12">
              Messages
            </q-item-section>

            <q-item-section>
              <q-badge rounded color="red-8" label="999+" style="max-width: 40px; margin-left: 40px;" />
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section class="text-h12">
              Logs
            </q-item-section>

            <q-item-section>
              <q-badge rounded color="blue-8" label="999+" style="max-width: 40px; margin-left: 40px;" />
            </q-item-section>
          </q-item>

        </q-card-section>
        <q-separator inset />
        <q-card-actions align="around">
          <q-btn flat to="/LockScreen">LockApp</q-btn>
          <q-btn flat v-on:click='authStore.logout()' >Logout</q-btn>
        </q-card-actions>

      </q-card>

    </q-menu>
  </q-btn>

</template>

<script lang="ts">
  import { defineComponent } from 'vue';
  import { LocalStorage } from 'quasar'
  import { useAuthStore } from 'stores/auth';


  export default defineComponent({
    name: 'ProfileMenu',
    setup() {
      const userData = LocalStorage.getItem('userData')
      const authStore = useAuthStore()
      return { 
        userData, 
        authStore, 
      };
    },
  });
</script>
