<template>
   <div class="q-pa-md">
      <q-list class="rounded-borders text-primary">
         <q-item
            clickable
            v-ripple
            to="/Dashboard/"
            :active="link === 'dashboard'"
            @click="link = 'dashboard'"
            active-class="principal_menu_active"
            >
            <q-item-section avatar>
               <q-icon name="dashboard" />
            </q-item-section>
            <q-item-section>Dashboard</q-item-section>
         </q-item>
         <!-- USERS -->
         <q-expansion-item
            icon="manage_accounts"
            label="Users"
            >
            <q-list class="q-pl-lg">
               <q-item 
                  to="/Users/" 
                  :active="link === 'users_list'"
                  @click="link = 'users_list'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="group"/>
                  </q-item-section>
                  <q-item-section>
                     <q-item-label>List Users</q-item-label>
                  </q-item-section>
               </q-item>
            </q-list>
            <q-list class="q-pl-lg">
               <q-item 
                  to="/Users/Add/" 
                  :active="link === 'users_add'"
                  @click="link = 'users_add'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="person_add"/>
                  </q-item-section>
                  <q-item-section>
                     <q-item-label>Add Users</q-item-label>
                  </q-item-section>
               </q-item>
            </q-list>
         </q-expansion-item>
         <!-- PRODUCTS -->
         <q-expansion-item
            icon="storefront"
            label="Products"
            >
            <q-list class="q-pl-lg">
               <q-item 
                  to="/Products/" 
                  :active="link === 'products_list'"
                  @click="link = 'products_list'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="list"/>
                  </q-item-section>
                  <q-item-section>
                     <q-item-label>Products List</q-item-label>
                  </q-item-section>
               </q-item>
            </q-list>
            <q-list class="q-pl-lg">
               <q-item 
                  to="/Products/Add/" 
                  :active="link === 'products_add'"
                  @click="link = 'products_add'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="add_business"/>
                  </q-item-section>
                  <q-item-section>
                     <q-item-label>Products Add</q-item-label>
                  </q-item-section>
               </q-item>
            </q-list>
         </q-expansion-item>
         <!-- ORDERS -->
         <q-expansion-item
            icon="receipt_long"
            label="Orders"
            >
            <q-list class="q-pl-lg">
               <q-item 
                  to="/Orders/" 
                  :active="link === 'orders_list'"
                  @click="link = 'orders_list'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="list_alt"/>
                  </q-item-section>
                  <q-item-section>
                     <q-item-label>Orders List</q-item-label>
                  </q-item-section>
               </q-item>
            </q-list>
            <q-list class="q-pl-lg">
               <q-item 
                  to="/Orders/Add/" 
                  :active="link === 'orders_add'"
                  @click="link = 'orders_add'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="playlist_add"/>
                  </q-item-section>
                  <q-item-section>
                     <q-item-label>Orders Add</q-item-label>
                  </q-item-section>
               </q-item>
            </q-list>
         </q-expansion-item>
         <!-- MAPS -->
         <q-expansion-item
            icon="map"
            label="Maps"
            >
            <q-list class="q-pl-lg">
               <q-item
                  clickable
                  v-ripple
                  to="/MapSimple/"
                  :active="link === 'map'"
                  @click="link = 'map'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="pin_drop" />
                  </q-item-section>
                  <q-item-section>Map</q-item-section>
               </q-item>
               <q-item
                  clickable
                  v-ripple
                  to="/MapMoving/"
                  :active="link === 'map_moving'"
                  @click="link = 'map_moving'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="mode_of_travel" />
                  </q-item-section>
                  <q-item-section>Map Moving</q-item-section>
               </q-item>
               <q-item
                  clickable
                  v-ripple
                  to="/MapCluster/"
                  :active="link === 'map_cluster'"
                  @click="link = 'map_cluster'"
                  active-class="principal_menu_active"
                  >
                  <q-item-section avatar>
                     <q-icon name="share_location" />
                  </q-item-section>
                  <q-item-section>Map Cluster</q-item-section>
               </q-item>
            </q-list>
         </q-expansion-item>
         <q-item
            clickable
            v-ripple
            to="/Others/"
            :active="link === 'others'"
            @click="link = 'others'"
            active-class="principal_menu_active"
            >
            <q-item-section avatar>
               <q-icon name="dynamic_feed" />
            </q-item-section>
            <q-item-section>Others</q-item-section>
         </q-item>
         <q-separator spaced />
         <q-item
            clickable
            v-ripple
            to="/Profile"
            :active="link === 'profile'"
            @click="link = 'profile'"
            active-class="principal_menu_active"
            >
            <q-item-section avatar>
               <q-icon name="settings" />
            </q-item-section>
            <q-item-section>Profile</q-item-section>
         </q-item>
         <q-item
            clickable
            v-ripple
            :active="link === 'help'"
            @click="link = 'help'"
            active-class="principal_menu_active"
            >
            <q-item-section avatar>
               <q-icon name="help" />
            </q-item-section>
            <q-item-section>Help</q-item-section>
         </q-item>
         <q-item
            clickable
            v-ripple
            to="/"
            :active="link === 'logout'"
            @click="authStore.logout()"
            active-class="principal_menu_active"
            >
            <q-item-section avatar>
               <q-icon name="logout" />
            </q-item-section>
            <q-item-section>Logout</q-item-section>
         </q-item>
      </q-list>
   </div>
</template>
<script>
   import { ref } from 'vue'
   import { useRoute } from 'vue-router';
   import { useAuthStore } from 'stores/auth';
   
   export default {
     watch: {
      '$route'(value) {
       this.link = value.name
     }
   },
   setup () {
     const routeName = useRoute().name
     const authStore = useAuthStore()
     return {
       link: ref(routeName),
       authStore,
     }
   }
   }
</script>