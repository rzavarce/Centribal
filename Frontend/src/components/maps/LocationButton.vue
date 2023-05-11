<template>
  <LControl
    class="leaflet-control leaflet-demo-control"
    position="topleft"
    >
    <button class="location_button" title="My location" @click="onLocationFound">
      <img src="my_location.svg" style="width: 20px; height:20px" >
    </button>
  </LControl>

  <LCircleMarker 
  :visible="location.visible" 
  :lat-lng="location.coords" 
  :radius="location.radius"
  :color="location.color" 
  >
  <LPopup> 
    <p><b>Address:</b> {{ location.message.address }}, {{ location.message.county_country }}. {{ location.message.zip_code }}</p> 
    <p><a :href="location.message.link" target="_blank">How to get to</a></p>
  </LPopup>

  </LCircleMarker>

</template>

<script lang="ts">
  import { defineComponent } from 'vue'
  import { Loading } from 'quasar'

  import { httpClient } from '../../helpers/httpClient.js'

  import { 
    LCircleMarker,
    LPopup, 
    LControl,
  } from '@vue-leaflet/vue-leaflet'


  export default defineComponent({
    name: 'LocationButton',
    components: {
      LCircleMarker,
      LPopup, 
      LControl,
    },
    props: {
      location: {
        type: Object,
        required: true
      },
      map: {
        type: Object,
        required: true
      },
    },
    methods: {
      onLocationFound(){
        Loading.show()
        let position = this.location
        this.map.locate({setView : true}).on('locationfound', function(location){
          Loading.hide()
          position.coords=[location.latitude, location.longitude]
          position.radius=location.accuracy + 10
          position.visible=true

          let url = 'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=' + location.latitude +'&lon=' + location.longitude
          httpClient.post(url, {}, false, false, false).then((response) => {
            position.message.address = `${response.address.road}, # ${response.address.house_number}`
            position.message.county_country = `${response.address.quarter}, ${response.address.state} - ${response.address.country}`
            position.message.zip_code = response.address.postcode
            position.message.link = `https://www.google.com/maps?saddr=My+Location&daddr=${response.address.road}, Num. ${response.address.house_number}, ${response.address.state} - ${response.address.country}`
          })

        })
      },
    }

  })

</script>