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
          <q-input
            filled
            v-model="product.name"
            label="Name"
            hint="Insert product name"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Product name is required.']"
          />
          <q-input
            filled
            v-model="product.description"
            type="textarea"
            label="Description"
            hint="Insert product name"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Product name is required.']"
          />
          <q-input
            filled
            v-model="product.price"
            label="Price"
            mask="#.##"
            fill-mask="0"
            reverse-fill-mask            
            suffix="EUR"
            hint="Product price with decimal"
            :rules="[ val => val && val > 0.00 || 'Product price is required.']"
            input-class="text-right"
          />
          <q-input
            filled
            v-model="product.tax"
            label="Taxes"
            mask="#.##"
            fill-mask="0"
            reverse-fill-mask
            hint="Product tax in percent, can be 0.00"
            suffix="%"
            input-class="text-right"
          />
          <q-input
            filled
            v-model="product.stock"
            label="Stock"
            type="number"
            hint="Product stock is required"
            :rules="[ val => val || 'Product stock is required.']"
          />
          <q-toggle 
            v-model="product.status"
            checked-icon="check"
            label="Status"
            color="green-8" 
            unchecked-icon="clear"
          />
          <q-separator />
          <q-btn-group spread>
            <q-btn label="Save" type="submit" color="green-7" />
            <q-btn label="Reset" type="reset" color="blue-7" />
            <q-btn label="Cancel" type="button" color="red-7" @click="$router.replace('/Products/')"/>
          </q-btn-group>
          </q-form>
        </div>
        <div class="col-xs-12 col-sm-4 columns-history">
          <q-timeline color="secondary">
            <q-timeline-entry heading >
              <span class="text-h5">Timeline History</span>
              <q-separator />
            </q-timeline-entry>
            <q-timeline-entry
              v-for="(product_history, index) in product_history"
              :key="index"
              :title="product_history.title"
              :subtitle="product_history.date" 
              :color="product_history.color" 
              :icon="product_history.icon"
              :side="product_history.side"
              >
              <div>{{ product_history.description }}</div>
              <div class="text-caption"><b>By user:</b> {{ product_history.by_user }}</div>
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
        product: {
        },
        product_history:{},
      }
    },
    methods: {

      async onSubmitForm() {
        
        const pk = this.$route.params.id
        httpClient.put('products/' + pk + '/', this.product)
      
      },
      onResetForm () {
        resetModelForm(this.product)
      },
      onValidationError(ref) {
        scrollToError(ref)
      }
    },
    mounted () {

      const pk = this.$route.params.id
     
      httpClient.get('products/edit/' + pk + '/', {}, false, false, false).then((response) => {
        this.product = response.product_data[0]
        this.product_history = setHistoryData(response.products_history, 'Products', 'name')
      })

    },
    setup() {

      return {
        title: 'Products Edit',
        caption: 'Update a product.',
        breadcrumsLinks: [
        {
          label: 'Dashboard',
          color: 'indigo',
          icon: 'dashboard',
          link: '/Dashboard'
        },
        {
          label: 'Products',
          color: 'indigo',
          icon: 'list',
          link: '/Products'
        },
        {
          label: 'Edit',
          color: 'indigo',
          icon: 'storefront',
          link: ''
        },
        ],

        
      }
    }
  })

</script>

