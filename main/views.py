from django.shortcuts import render
from django.core.mail import send_mail



def index(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_phone = request.POST['message-phone']
		message_text = request.POST['message-text']

		# Send an email
		send_mail(
			'Заказ от: ' + message_name, # subject
			'Телефон: ' + message_phone + '\n' + 'Заказ: ' + message_text, # message
			message_phone, # from
			['organic.smr@gmail.com'], # to email
			)

		return render(request, 'main/contact.html', {'message_name' : message_name})

	else:
		return render(request, 'main/index.html', {})


def about(request):
	return render(request, 'main/about.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_phone = request.POST['message-phone']
		message_adress_street = request.POST['message-adress-street']
		message_adress_house = request.POST['message-adress-house']
		message_adress_flat = request.POST['message-adress-flat']
		message_text = request.POST['message-text']

		# Send an email
		send_mail(
			'Заказ от: ' + message_name, # subject
			'Телефон: ' + message_phone + '\n' + 'Адрес: ' + 'Улица: ' + message_adress_street + ' Дом: ' + message_adress_house + ' Квартира: ' + message_adress_flat + '\n' + 'Заказ: ' + message_text, # message
			message_phone, # from
			['vanyajet@gmail.com'], # to email
			)

		return render(request, 'main/contact.html', {'message_name' : message_name})

	else:
		return render(request, 'main/contact.html', {})
