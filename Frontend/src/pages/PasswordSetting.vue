<template>
	<q-layout>
		<q-page-container>
			<q-page class="flex bg-image flex-center">
				<q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}">
					<q-card-section>
						<q-avatar size="103px" class="absolute-center shadow-10">
							<img src="../assets/profile.svg">
						</q-avatar>
					</q-card-section>
					<q-card-section>
						<div class="text-center q-pt-lg">
							<div class="col text-h6 ellipsis">
								Password Setting
							</div>
						</div>
					</q-card-section>
					<q-card-section>
						<q-form
						greedy
						class="q-gutter-md"
						@submit="onPasswordSetting"
						>
						<q-input
						type="password"
						filled
						v-model="password_setting.password"
						label="New Password"
						hint="Insert your new Password"
						lazy-rules
						:rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.']"
						/>

						<q-input
						type="password"
						filled
						v-model="password_setting.password_confirm"
						label="Renew Password"
						hint="Confirm your new Password"
						lazy-rules
						:rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.', 
						val => val && val==password_setting.password_confirm || 'Passwords not match']"
						/>

						<q-input
						filled
						v-model="password_setting.user"
						lazy-rules
						style="display:none;"
						/>
						<div class="row justify-center">
							<q-btn label="Send Reset Password" type="submit" color="primary" />
						</div>
						<div class="row justify-center" style="margin:20px;">  
							<q-btn flat color="primary" label="Go to Login" to="/" />
						</div>
					</q-form> 

				</q-card-section>


			</q-card>
		</q-page>
	</q-page-container>
</q-layout>	

</template>

<script lang="ts">
	import { defineComponent } from 'vue';
	import { httpClient } from '../helpers/httpClient.js'
	import { resetModelForm, } from '../helpers/utils.js'

	export default defineComponent({
		name: 'PasswordSetting',
		data () {
			return {
				password_setting: {
					password: '',
					password_confirm: '',
					user: this.$route.params.user,	
				},		
			}
		},
		methods: {
			onResetForm () {
				resetModelForm(this.password_setting)
			},
			onPasswordSetting() {

				const payload = {
					'password': this.password_setting.password,
					'user': this.password_setting.user
				}

				httpClient.post('users/setpassword/', payload)
			},
		},
	});
</script>


