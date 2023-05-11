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
          @ready="onMapReady" 
        >
          <l-control-layers position="topright"></l-control-layers>
          <LTileLayer
            v-for="tileProvider in tileProviders"
            :key="tileProvider.name"
            :name="tileProvider.name"
            :visible="tileProvider.visible"
            :url="tileProvider.url"
            :attribution="tileProvider.attribution"
            layer-type="base"
          >

          </LTileLayer>

          <l-control
            class="leaflet-control leaflet-demo-control"
            position="topleft"
          >
            <q-btn
              @click="moving"
              icon="map"
              class="fullscreen_button"
            />
          </l-control>

          <l-control
            class="leaflet-control leaflet-demo-control"
            position="topleft"
          >
            <q-btn
              @click="fullscreen_toggle"
              :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
              class="fullscreen_button"
            />
          </l-control>

          <l-control
            class="leaflet-control leaflet-demo-control"
            position="topleft"
          >
            <button class="location_button" title="My location" @click="onLocationFound">
              <img src="https://i.ibb.co/NjqgbWn/my-location.png" alt="my-location" style="width: 20px; height:20px" >
            </button>
          </l-control>

          <LMarker :lat-lng="marker.coords" ref="markerRef">
            <LIcon 
              :icon-url="icon.url" 
              :icon-size="icon.size" 
              :icon-anchor="icon.anchor"
              :popup-anchor="icon.popup"
            />
            
            <LTooltip> Hi! You can drag me around! </LTooltip>
            <LPopup> Hey! Polyline here, at your service! </LPopup>
          </LMarker>

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

          <LControlAttribution
            position="bottomright"
            :prefix="mapSet.customAttributionPrefix"
          />
          <LControlScale position="bottomleft" :imperial="false" :metric="true" />
          
        </LMap>
      </div>
    </q-card-section>
  </q-card>

</template>

<script lang="ts">
  import { defineComponent, ref } from 'vue'
  import { Loading } from 'quasar'
  import useQuasar from 'quasar/src/composables/use-quasar.js';

  import { httpClient } from '../../helpers/httpClient.js'

  import 'leaflet/dist/leaflet.css'
  // import L from 'leaflet'

  import { 
    LMap, 
    LTileLayer,
    LControlLayers, 
    LMarker, 
    LIcon, 
    LCircleMarker,
    LPopup, 
    LTooltip, 
    LControl,
    LControlScale, 
    LControlAttribution 
  } from '@vue-leaflet/vue-leaflet'


  import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch'
  import 'leaflet-geosearch/dist/geosearch.css'


  export default defineComponent({
    name: 'MapPage',
    components: {
      LMap,
      LTileLayer,
      LControlLayers,
      LMarker,
      LIcon,
      LCircleMarker,
      LTooltip,
      LPopup,
      LControl,
      LControlScale,
      LControlAttribution,
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
        tileProviders: [
          {
            name: 'OpenStreetMap',
            visible: true,
            attribution:
              '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
          },
          {
            name: 'OpenTopoMap',
            visible: false,
            url: 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
            attribution:
              'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
          },
          {
            name: 'OpenEsriMap',
            visible: false,
            url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attribution:
              'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
          },
        ],
        icon: {
          url: 'https://s3-eu-west-1.amazonaws.com/ct-documents/emails/A-static.png',
          size: [23, 42],
          anchor: [13, 37],
          popup: [-2, -33],
        },
        marker: {
          coords: [47.41322, -1.219482],
          test: true,
        },
        location:{
          visible: false,
          coords: [0,0],
          radius: 10,
          color: 'blue',
          accuracy: 0,
          message: {
            address: '',
            county_country: '',
            zip_code: '',
            link: ''
          },
          position: {

          },
        }
      }
    },
    methods: {
      moving(){

        var duration = 0.5 //COLOCAR COMO PARAMETRO DE ENTRADA
        var keepAtCenter = false

        // OJOOOOOO DEBO COLOCAR COMO PARAMETRO DE ENTRADA LA NUEVA UBICACION
        if(this.marker.test){
          var new_coords = [47.453219, -1.759482]
          this.marker.test = false
        }else{
          var new_coords = [47.41322, -1.219482]
          this.marker.test = true
        }

        var map = this.mapSet
        var marker = this.marker
        var deltalat = (new_coords[0] - marker.coords[0]) / 100
        var deltalng = (new_coords[1] - marker.coords[1]) / 100
        var delay = 10 * duration

        for (var i = 0; i < 100; i++) {
          (function(ind) {
            setTimeout(
              function() {
                var lat = marker.coords[0]
                var lng = marker.coords[1]
                lat += deltalat
                lng += deltalng
                marker.coords = [lat, lng]

                if(keepAtCenter) 
                  map.center = [lat, lng]

              }, delay * ind
            )
          })(i)
        }

      },
      onMapReady(map) {

        this.mapRef = map
        this.map = map
        const searchControl = GeoSearchControl({
          provider: new OpenStreetMapProvider(),
          style: 'button',
          autoClose: true,
          showMarker: true,
          autoComplete: true,
          autoCompleteDelay: 250,
        });

        map.addControl(searchControl)

        // OJO ESTO ES PARA CONTROLAR CUANDO EL MAPA SE MUEVE 
        map.on('move', () => {
          console.log('map was moved')
          let zoom = map.getZoom()

          if(zoom > 12 && this.location.radius > 10){ 
            this.location.radius *= zoom/30 
          }else{
            this.location.radius = this.location.accuracy * zoom/30 
          }

        })

      },
      onLocationFound(){
        Loading.show()
        let position = this.location
        let map = this.map
        map.locate({setView : true}).on('locationfound', function(location){
          Loading.hide()
          position.coords=[location.latitude, location.longitude]
          position.radius=location.accuracy + 10
          position.accuracy=location.accuracy
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
    },
    setup() {
      const $q = useQuasar()
      return {
        mapRef: ref('mapRef'),
        markerRef: ref('markerRef'),
        // mapRef: ref<any>('mapRef'),
        fullscreen_toggle (e) {

          const target = e.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode

          $q.fullscreen.toggle(target)

        }
      }
    }
  });

</script>
