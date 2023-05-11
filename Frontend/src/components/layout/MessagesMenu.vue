<template>
  <q-btn round dense flat color="white" icon="notifications" title="Notifications">
    <q-badge color="red" text-color="white" floating>
      5
    </q-badge>
    <q-menu>
      <q-list style="min-width: 100px">
        <div>
          <q-item style="max-width: 420px" v-for="msg in messages" :key="msg.id" clickable v-ripple>
            <q-item-section avatar>
              <q-avatar>
                <img :src="msg.avatar">
              </q-avatar>
            </q-item-section>

            <q-item-section>
              <q-item-label>{{ msg.name }}</q-item-label>
              <q-item-label caption lines="1">{{ msg.msg }}</q-item-label>
            </q-item-section>

            <q-item-section side>
              {{ msg.time }}
            </q-item-section>
          </q-item>
        </div>
        <q-card class="text-center no-shadow no-border">
          <q-btn label="View All" style="max-width: 120px !important;" flat dense
          class="text-indigo-8"></q-btn>
        </q-card>
      </q-list>
    </q-menu>
  </q-btn>
</template>

<script>
  import {defineComponent} from 'vue'

  export default defineComponent({
    name: 'MessagesMenu',
    setup() {
      return {
        messages: [
        {
          id: 5,
          name: 'Pratik Patel',
          msg: ' -- I\'ll be in your neighborhood doing errands this\n' +
          '            weekend. Do you want to grab brunch?',
          avatar: 'https://avatars2.githubusercontent.com/u/34883558?s=400&v=4',
          time: '10:42 PM'
        }, {
          id: 6,
          name: 'Winfield Stapforth',
          msg: ' -- I\'ll be in your neighborhood doing errands this\n' +
          '            weekend. Do you want to grab brunch?',
          avatar: 'https://cdn.quasar.dev/img/avatar6.jpg',
          time: '11:17 AM'
        }, {
          id: 1,
          name: 'Boy',
          msg: ' -- I\'ll be in your neighborhood doing errands this\n' +
          '            weekend. Do you want to grab brunch?',
          avatar: 'https://cdn.quasar.dev/img/boy-avatar.png',
          time: '5:17 AM'
        }, {
          id: 2,
          name: 'Jeff Galbraith',
          msg: ' -- I\'ll be in your neighborhood doing errands this\n' +
          '            weekend. Do you want to grab brunch?',
          avatar: 'https://cdn.quasar.dev/team/jeff_galbraith.jpg',
          time: '5:17 AM'
        }, {
          id: 3,
          name: 'Razvan Stoenescu',
          msg: ' -- I\'ll be in your neighborhood doing errands this\n' +
          '            weekend. Do you want to grab brunch?',
          avatar: 'https://cdn.quasar.dev/team/razvan_stoenescu.jpeg',
          time: '5:17 AM'
        }
        ],
      }
    }
  })
</script>

<style scoped>

</style>