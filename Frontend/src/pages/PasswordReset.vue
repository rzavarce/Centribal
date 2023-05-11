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
								Password Reset
							</div>
						</div>
					</q-card-section>
					<q-card-section>
					<q-form
					greedy
					class="q-gutter-md"
					@submit="onPasswordReset"
					>
					<q-input
					type="password"
					filled
					v-model="password"
					label="New Password"
					hint="Insert your new Password"
					lazy-rules
					:rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.']"
					/>

					<q-input
					type="password"
					filled
					v-model="passwordConfirmation"
					label="Renew Password"
					hint="Confirm your new Password"
					lazy-rules
					:rules="[ val => val && val.length >= 8 || 'Password length must be atleast 8 characters.']"
					/>

					<q-input
					type="password"
					filled
					v-model="user"
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
	import { useAuthStore } from 'stores/auth';

	export default defineComponent({
		name: 'PasswordReset',
		data () {
			return {
				password: '',
				passwordConfirmation: '',
				user: this.$route.params.user,
				passwordResetError: false,
			}

		},
		methods: {

			async onPasswordReset() {

        		await this.authStore.passwordReset(this.password, this.passwordConfirmation, this.user)

			},

		},

		setup() {

			const authStore = useAuthStore();

			return { 
				authStore, 

			};
		},
	});
</script>


