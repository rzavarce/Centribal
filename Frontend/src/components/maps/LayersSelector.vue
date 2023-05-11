<template>
  <LControlLayers position="topright" />
  <LTileLayer
    v-for="tileProvider in tileProviders"
    :key="tileProvider.name"
    :name="tileProvider.name"
    :visible="tileProvider.visible"
    :url="tileProvider.url"
    :attribution="tileProvider.attribution"
    layer-type="base"
  />
</template>

<script lang="ts">
import { defineComponent } from 'vue'

  import { 
    LTileLayer,
    LControlLayers
  } from '@vue-leaflet/vue-leaflet'

export default defineComponent({
  name: 'LayersSelector',
  components: {
    LTileLayer,
    LControlLayers
  },
  data() {
      return {

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

      }
    },
});
</script>