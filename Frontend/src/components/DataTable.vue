<template>
  <q-table
  flat 
  bordered
  virtual-scroll
  row-key="name"
  class="my-sticky-header-column-table"
  :dense="$q.screen.lt.md"
  :rows="rows"
  :columns="columns"
  :filter="filter"
  :grid="mode=='grid'"
  :hide-header="mode === 'grid'"
  :pagination="pagination"
  :separator="separator.value"
  >
  <template v-slot:top-left>
    <q-btn
    color="green-7"
    icon="add_box"
    label="Add new"
    no-caps
    @click="addRow"
    class="q-ml-xs"
    />
  </template>
  <template v-slot:top-right="props">

    <q-select
      dense
      label="Table Separator" 
      style="width: 120px; margin: 5px;"
      v-model="separator"
      :options="[
        { label: 'Horizontal', value: 'horizontal' },
        { label: 'Vertical', value: 'vertical' },
        { label: 'Cell', value: 'cell' },
        { label: 'None', value: 'none' },
      ]"
    />

    <q-input outlined dense debounce="300" v-model="filter" placeholder="Search" style="margin: 5px;">
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>

    <div class="data_table_buttons">
    <q-btn
    flat round dense
    :icon="props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
    @click="props.toggleFullscreen"
    class="q-ml-md"
    >
    <q-tooltip>Fullscreen</q-tooltip>
  </q-btn>
  <q-btn
  flat
  round
  dense
  :icon="mode === 'grid' ? 'list' : 'grid_on'"
  @click="mode = mode === 'grid' ? 'list' : 'grid'; separator = mode === 'grid' ? 'none' : 'horizontal'"
  >
  <q-tooltip>{{mode==='grid' ? 'List' : 'Grid'}}</q-tooltip>
</q-btn>
<q-btn
flat
round
dense
icon="archive"
@click="exportTable()"
>
<q-tooltip>Export to csv</q-tooltip>
</q-btn>
</div>
</template>
<template #body-cell-status="props">
  <q-td :props="props" v-if="props.row.status">
    <q-badge 
      :color="props.row.status ? 'green' : 'grey'"
      :label=" props.row.status ? 'Active' : 'Disable'"
    />
  </q-td>
</template>
<template #body-cell-action="props">
  <q-td :props="props">
    <q-btn round dense color="blue-7" icon="edit" @click="editRow(props)" style="font-size: 0.8em!important" /> <span></span>
    <q-btn round dense color="red" icon="delete" @click="deleteRow(props)" style="font-size: 0.8em!important" />
  </q-td>
</template>
<template v-slot:item="props">
  <div
  class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3 grid-style-transition"
  :style="props.selected ? 'transform: scale(0.95);' : ''"
  >
  <q-card :class="props.selected ? 'bg-grey-2' : ''">
    <q-list dense>
      <q-item v-for="col in props.cols" :key="col.name">
        <q-item-section>
          <q-item-label>{{ col.label }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-badge 
            v-if="col.name === 'status'"
            :color="props.row.status ? 'green' : 'grey'"
            :label=" props.row.status ? 'Active' : 'Disable'"
          />
          <div v-else-if="col.name === 'action'" style="margin-right: -10px;">
            <q-btn dense round color="blue-7" icon="edit" @click="editRow(props)" />
            <q-btn dense round color="red" icon="delete" @click="deleteRow(props)"/>
          </div>
          <q-item-label v-else caption :class="col.classes ? col.classes : ''">{{ col.value }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-card>
</div>
</template>
</q-table>

</template>

<script lang="ts">
  import { defineComponent, ref } from 'vue'
  import { Dialog } from 'quasar'
  import exportFromJSON from 'export-from-json'
  import { capitalize } from '../helpers/utils.js'
  import { httpClient } from '../helpers/httpClient.js'


  export default defineComponent({
    name: 'DataTable',
    props: {
      columns: {
        type: Array,
        required: true
      },
      rows: {
        type: Array,
        required: true
      },
      module: {
        type: String,
        required: true
      },
    },
    data() {
      return {
        mode: 'list',
        rowsData: this.rows,
        pagination: {
          rowsPerPage: 10
        }
      }
    },
    
    methods: {
      addRow() {
        this.$router.replace('/' + capitalize(this.module)+ '/Add/')
      },
      editRow(props) {
        this.$router.replace('/' + capitalize(this.module) + '/Edit/' + props.row.id + '/')
      },
      deleteRow(props){
        Dialog.create({
          title: 'Confirm',
          message: 'Do you want to delete this register?',
          cancel: true,
          persistent: true
        }).onOk(() => {
          httpClient.delete(this.module + '/' + props.row.id + '/').then(() => {
            this.rowsData.splice(this.rowsData.indexOf(props.row),1)            
          })
        })
      },
      exportTable () {
        const data = this.rowsData
        const fileName = this.module + '_export'
        const exportType = exportFromJSON.types.xls
        if (data) exportFromJSON({ data, fileName, exportType })
      }  
    }, 
    setup() {
      return {
        filter: ref(''),
        separator: ref({ label: 'Horizontal', value: 'horizontal' }),
      }
    }

  });
</script>
<style>
.q-dialog-plugin {
  background-color: #c10015;
  color: white;
}

</style>
