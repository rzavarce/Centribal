import { date } from 'quasar'
import { scroll } from 'quasar'
const { getScrollTarget, setVerticalScrollPosition } = scroll


function emailValidation (val) {
	if(val.length == 0) return 'Email field is empty'
		const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
	return emailPattern.test(val) || 'Please enter a valid email address'
}

function scrollToError(element){
	const el = element.$el
	console.log(el)
	setVerticalScrollPosition(getScrollTarget(el), el.offsetTop + 90, 500)
}

function resetModelForm(model){
	if(model){
		Object.keys(model).forEach((i) => {			
			switch (typeof(model[i])) {
			  case 'string':
			    model[i] = null
			    break;
			  case 'number':
			    model[i] = 0
			    break;
			  case 'boolean':
			    model[i] = false
			    break;
			}

		})
	}
	const el = document.querySelector('.q-page-container')
	setVerticalScrollPosition(getScrollTarget(el), 0, 500)
}

function capitalize(str){
	return str.charAt(0).toUpperCase() + str.slice(1)
}

const historyTypesParser = function (modeName) {

	return {
		'+': {
			'icon': 'add',
			'color': 'green',
			'description': 'New ' + modeName +' register has been added.',
		},
		'~': {
			'icon': 'edit',
			'color': 'blue',
			'description': modeName +' register has been updated.',
		},
		'-': {
			'icon': 'clear',
			'color': 'red',
			'description': modeName +' Register has been deleted.',
		}
	}

}


function setHistoryData(historyModel, modelName, title){

	let historyTypes = historyTypesParser(modelName)

	historyModel.forEach(function(object) {
		object.date = date.formatDate(object.history_date, 'YYYY/MM/DD HH:mm:ss')
		object.title = object[title]
		object.description = historyTypes[object.history_type].description
		object.color = historyTypes[object.history_type].color
		object.icon = historyTypes[object.history_type].icon
		object.by_user = object.history_user ? object.history_user.username : 'Undefined'
	})
	return historyModel

}


export { emailValidation, scrollToError, resetModelForm, setHistoryData, capitalize }


