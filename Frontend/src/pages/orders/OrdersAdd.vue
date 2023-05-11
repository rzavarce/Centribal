<template>
  <q-card bordered>
    <q-card-section>
      <BreadCrums
      :title="title"
      :caption="caption"
      :breadcrumsLinks="breadcrumsLinks"
      />
    </q-card-section>
    <q-separator />
    <q-card-section>

      <div class="row">
        <div class="col-xs-12 col-sm-8 columns-forms">
          <q-form
          greedy
          class="q-gutter-md"
          @submit="onSubmitForm"
          @reset="onResetForm"
          @validation-error="onValidationError"
          >
          <div class="row" style="margin-bottom: 10px;">
            <div class="col-6">
              <q-select
              filled
              clearable
              emit-value
              map-options
              v-model="client"
              :options="clients_list"
              label="Client *"
              hint="Select a client"
              behavior="menu"
              lazy-rules                  
              style="margin:3px;"
              />
            </div>
            <div class="col-3">
              <q-input 
              filled 
              v-model="today" 
              disable 
              hint="Today"
              mask="##/##/####"
              style="margin:3px;"
              />
            </div>   
            <div class="col-3">
              <q-btn
              color="green-7"
              icon="add_box"
              label="Add new product"
              no-caps
              @click="addRow"
              class="q-ml-xs"
              style="margin:3px;"
              />
            </div>
          </div>
          <q-separator />
          <div class="previous"
          v-for="(product, counter) in order_detail"
          v-bind:key="counter">

          <div class="row">
            <div class="col-4">
              <q-select
              filled
              clearable
              emit-value
              map-options
              v-model="product.id"
              :options="products_list"
              label="Products *"
              hint="Select a product"
              behavior="menu"
              lazy-rules                  
              :rules="[ val => val && val != null || 'Product is required.']"
              style="margin:3px;"
              @update:model-value="val => onValueChange(val)"
              />
            </div>
            <div class="col-3">
              <q-input
              filled
              v-model.number="product.quantity"
              label="Quantity"
              type="number"
              hint="Quantity"
              :rules="[ val => val  && val > 0 || 'Required.']"
              style="margin:3px;"
              />
            </div>
            <div class="col-2">
              <q-input
              filled
              v-model="price[counter]"
              label="Price"         
              suffix="EUR"
              hint="Price"
              input-class="text-right"
              disable
              style="margin:3px;"
              />
            </div>
            <div class="col-2">
              <q-input
              filled
              v-model="tax[counter]"
              label="Taxes"
              mask="#.##"
              fill-mask="0"
              reverse-fill-mask
              hint="Taxes"
              suffix="%"
              input-class="text-right"
              disable
              style="margin:3px;"
              />
            </div>
            <div class="col-1">
              <q-btn 
              round 
              @click="deleteRow(counter)" 
              color="red" 
              icon="delete" 
              style="margin: 10px 5px 15px 10px;"
              />
            </div>
          </div>
        </div>
        <p v-if="isValid" style="color:red">Fileds are empty, please fill alls fields in the row.</p>
        <q-separator />
        <q-btn-group spread>
          <q-btn label="Save" type="submit" color="green-7" />
          <q-btn label="Reset" type="reset" color="blue-7" />
          <q-btn label="Cancel" type="button" color="red-7" @click="$router.replace('/Orders/')"/>
        </q-btn-group>
      </q-form>
    </div>
    <div class="col-xs-12 col-sm-4 columns-history">
      <q-timeline color="secondary">
        <q-timeline-entry heading >
          <span class="text-h4">Timeline History</span>
          <q-separator />
        </q-timeline-entry>
        <q-timeline-entry
        v-for="(orders_history, index) in orders_history"
        :key="index"
        :title="orders_history.title"
        :subtitle="orders_history.date" 
        :color="orders_history.color" 
        :icon="orders_history.icon"
        :side="orders_history.side"
        >
        <div>{{ orders_history.description }}</div>
        <div class="text-caption"><b>By user:</b> {{ orders_history.by_user }}</div>
      </q-timeline-entry>
    </q-timeline>
    <q-btn flat color="primary" label="See alls" to="/history" />
  </div>
</div>
</q-card-section>
</q-card>
</template>
<script>
  import { defineComponent } from 'vue'
  import { date } from 'quasar'
  import BreadCrums from 'components/layout/BreadCrums.vue';
  import { httpClient } from '../../helpers/httpClient.js'
  import { scrollToError, resetModelForm, setHistoryData } from '../../helpers/utils.js'

  export default defineComponent({
    name: 'UserAdd',
    components: {
      BreadCrums,

    },
    data () {
      return {
        client: '',
        products_list: [],
        clients_list: [
          'Client Fake 0',
          'Client Fake 1',
          'Client Fake 2',
          'Client Fake 3',
          'Client Fake 4',
          ],
        order_detail: [
        {
          id: '',
          quantity: 0,
        }
        ],
        price: [0,],
        tax: [0,],
        counter: 0,
        isValid: false,
        orders_history:{},
      }
    },
    methods: {
      onValueChange(val){
        let selected = this.products_list.find(e => e.value === val)
        this.price[this.counter] = selected.price
        this.tax[this.counter] = selected.tax
      },
      
      addRow() {   

        if (this.order_detail[this.counter].id == '' || this.order_detail[this.counter].name == '' || this.order_detail[this.counter].quantity == '' ){

          this.isValid = true;

        }else{

          this.order_detail.push({
            id: '',
            quantity: '',
          });
          this.counter += 1;
          this.isValid = false;

        }
      },
      deleteRow(index){
        if(this.counter>0){

          this.order_detail.splice(index, 1);
          this.counter -= 1;
          this.isValid = false;

        }
      },

      async onSubmitForm() {

        const payload = JSON.stringify({'order_detail': this.order_detail})

        httpClient.post('orders/', payload).then(() => {
          this.onResetForm()
        })
        
      },
      onResetForm () {
        resetModelForm(this.order)
      },
      onValidationError(ref) {
        scrollToError(ref)
      }
    },
    mounted () {

      httpClient.get('orders/add/', {}, false, false, false).then((response) => {
        this.products_list = response.products_list
        this.orders_history = setHistoryData(response.orders_history, 'Orders', 'reference')
      })

    },
    setup() {
      let today = new Date()
      today = date.formatDate(today, 'DD/MM/YYYY/')
      return {
        today,
        title: 'Orders Add',
        caption: 'Update a order.',
        breadcrumsLinks: [
        {
          label: 'Dashboard',
          color: 'indigo',
          icon: 'dashboard',
          link: '/Dashboard'
        },
        {
          label: 'Orders',
          color: 'indigo',
          icon: 'list_alt',
          link: 'Orders'
        },
        {
          label: 'Add',
          color: 'indigo',
          icon: 'person_add',
          link: ''
        },
        ],

        
      }
    }
  })

</script>
