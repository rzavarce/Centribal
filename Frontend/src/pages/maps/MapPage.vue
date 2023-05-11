<template>
  <q-card bordered>
    <q-card-section>
      <div style="height:85vh; width:100%">
        <LMap
          ref="mapRef"
          v-model:zoom="mapSet.zoom" 
          :center="mapSet.center" 
          :options="{ attributionControl: false }"
          :zoomAnimation="true"
          :markerZoomAnimation="true"
          :use-global-leaflet="true"
          @ready="onMapReady" 
        >

        <LayersSelector />

          <LMarker :lat-lng="marker.coords">
            <LIcon 
              :icon-url="icon.url" 
              :icon-size="icon.size" 
              :icon-anchor="icon.anchor"
              :popup-anchor="icon.popup"
            />
            
            <LTooltip> Hi! You can drag me around! </LTooltip>
            <LPopup> Hey! Polyline here, at your service! </LPopup>
          </LMarker>

          <FullScreenButton />

          <LocationButton
            :location="location"
            :map="map"
          />

          <MapFooter />
          
        </LMap>
      </div>
    </q-card-section>
  </q-card>

</template>

<script lang="ts">
  import { defineComponent } from 'vue'
  import 'leaflet/dist/leaflet.css'

  import { 
    LMap, 
    LMarker, 
    LIcon, 
    LPopup, 
    LTooltip, 
  } from '@vue-leaflet/vue-leaflet'


  import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch'
  import 'leaflet-geosearch/dist/geosearch.css'

  
  import LocationButton from '../../components/maps/LocationButton.vue'
  import LayersSelector from '../../components/maps/LayersSelector.vue'
  import MapFooter from '../../components/maps/MapFooter.vue'
  import FullScreenButton from '../../components/maps/FullScreenButton.vue'

  export default defineComponent({
    name: 'MapPage',
    components: {
      LMap,
      LMarker,
      LIcon,
      LTooltip,
      LPopup,
      LocationButton,
      LayersSelector,
      MapFooter,
      FullScreenButton,
    },
    data() {
      return {
        map: LMap,
        mapSet: {
          url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          center: [47.41322, -1.219482],
          map_name: 'TestMap',
          layer: 'base',
          zoom: 10,
          customAttributionPrefix: '<b>By: Roger Zavarce</b>',
        },
        
        icon: {
          url: 'https://s3-eu-west-1.amazonaws.com/ct-documents/emails/A-static.png',
          size: [23, 42],
          anchor: [13, 37],
          popup: [-2, -33],
        },
        marker: {
          coords: [47.41322, -1.219482],
        },
        location:{
          visible: false,
          coords: [0,0],
          radius: 10,
          color: 'blue',
          message: {
            address: '',
            county_country: '',
            zip_code: '',
            link: ''
          },
        }
      }
    },
    methods: {
      onMapReady(map) {
        this.map = map
        const searchControl = GeoSearchControl({
          provider: new OpenStreetMapProvider(),
          style: 'button',
          autoClose: true,
          showMarker: true,
          autoComplete: true,
          autoCompleteDelay: 250,
        });

        map.addControl(searchControl);

      },      
    },
  });

</script>
