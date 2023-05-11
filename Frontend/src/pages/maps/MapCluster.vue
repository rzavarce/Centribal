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
          :useGlobalLeaflet="true"
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
          />

          <l-control
            class="leaflet-control leaflet-demo-control"
            position="topleft"
          >
            <q-btn
              @click="toggle"
              :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
              class="fullscreen_button"
            />
          </l-control>

          <l-control
            class="leaflet-control leaflet-demo-control"
            position="topleft"
          >
            <button class="location_button" title="My location" @click="onLocationFound">
              <img src="my_location.svg" style="width: 20px; height:20px" >
            </button>
          </l-control>

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
  import L from 'leaflet'

  import { 
    LMap, 
    LTileLayer,
    LControlLayers, 
    LCircleMarker,
    LPopup, 
    LControl,
    LControlScale, 
    LControlAttribution 
  } from '@vue-leaflet/vue-leaflet'


  import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch'
  import 'leaflet-geosearch/dist/geosearch.css'


  import { MarkerClusterGroup } from 'leaflet.markercluster'
  import 'leaflet.markercluster/dist/MarkerCluster.css'
  import 'leaflet.markercluster/dist/MarkerCluster.Default.css'


  export default defineComponent({
    name: 'MapPage',
    components: {
      LMap,
      LTileLayer,
      LControlLayers,
      LCircleMarker,
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

        map.addControl(searchControl);

        function r(min, max) {
          return Math.random() * (max - min) + min;
        }
        let markers = new MarkerClusterGroup()
        for (let i = 0; i < 15000; i++) {
          const marker = L.marker(
            L.latLng(r(47.01322, 47.91322), r(-1.019482, -1.619482))
          );
          marker.bindPopup('Number ' + i);
          // markers.push(marker);
          markers.addLayer(marker)
        }

        map.addLayer(markers)

        map.fitBounds(markers.getBounds());

      },
      onLocationFound(){
        Loading.show()
        let position = this.location
        this.map.locate({setView : true}).on('locationfound', function(location){
          Loading.hide()
          position.coords=[location.latitude, location.longitude]
          position.radius=location.accuracy + 10
          position.visible=true

          let url = 'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=' + location.latitude +'&lon=' + location.longitude
          console.log(url)
          httpClient.post(url, {}, false, false, false).then((response) => {
            console.log(response)
            //position.message = `Road: ${response.address.road}, Num. ${response.address.house_number}. ${response.address.postcode} <br> ${response.address.quarter} - ${response.address.state}`
            position.message.address = `${response.address.road}, # ${response.address.house_number}`
            position.message.county_country = `${response.address.quarter}, ${response.address.state} - ${response.address.country}`
            position.message.zip_code = response.address.postcode
            position.message.link = `https://www.google.com/maps?saddr=My+Location&daddr=${response.address.road}, Num. ${response.address.house_number}, ${response.address.state} - ${response.address.country}`

          })

        })
      },
    },
    mounted(){
      // this.map = this.$refs.MapView.mapObject;
      console.log(this.mapRef)

    },
    setup() {
      const $q = useQuasar()
      return {
        mapRef: ref('mapRef'),
        // mapRef: ref<any>('mapRef'),
        toggle (e) {

          const target = e.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode

          $q.fullscreen.toggle(target)

        }
      }
    }
  });

</script>
