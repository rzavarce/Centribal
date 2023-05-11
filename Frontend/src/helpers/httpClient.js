import { Notify } from 'quasar'
import { Loading } from 'quasar'
import { api } from 'boot/axios'
import { capitalize } from '../helpers/utils.js'

const httpClient = {
    get: request('get'),
    post: request('post'),
    put: request('put'),
    delete: request('delete')
}

function request(method) {
    return (
        url, 
        body = {}, 
        loading = true,
        notifyThen = true,
        notifyError = true    
        ) => {
            if (loading) Loading.show()
            return api[method](url, body)
            .then((response) => {
                if (loading) Loading.hide()
                if(notifyThen){
                    Notify.create({
                        color: 'green-4',
                        icon: 'check_circle',
                        multiLine: true,
                        message: 'Request has been successed.',
                    })
                }
                return response.data
            })
            .catch((error) => {
                console.log('error', error)
                if (loading) Loading.hide()
                    if(notifyError){
                        let message = error.message
                        let key_parsed = ''
                        if (error.response.status == 400){
                            message = ''
                            Object.keys(error.response.data).forEach(key => {

                                key_parsed = key == 'non_field_errors' ? 'Error' : capitalize(key) 
                                message += '<b>' + key_parsed + ':</b> ' + error.response.data[key][0] + '<br>'
                            
                            });
                        }
                        Notify.create({
                            color: 'negative',
                            message: message,
                            icon: 'report_problem',
                            html: true
                        })
                        return error
                    }
                })
            }
    }

export { httpClient }
