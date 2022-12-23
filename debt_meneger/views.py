from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .lib import lib_power, lib_age, subtract_lowns_from_debt
from .models import Transaction, Partner
from .serializers import TransactionSerializer, PartnerSerializer

def home_page(request):
	context = {'url_names':['display_all_partners',
							'add_debt',
							'add_partner',
							'display_partner_debt_sum', 
							'transaction_list', 
							'transaction_dtails',
							'partner_details']}

	return render(request, 'debt_meneger/home_page.html', context=context)

def add_debt(request):
	if request.method == "GET":	
		return render(request, 'debt_meneger/add_debt.html')

	if request.method == "POST":
		data = request.POST
		lowaner = Partner.objects.filter(name=data['lowaner'])
		debtor = Partner.objects.filter(name=data['debtor'])
		new_transaction = Transaction(lowaner=lowaner[0], debtor=debtor[0], mouny_moved=data['mouny_moved'], resone=data['resone'], date=data['date'])
		new_transaction.save()
		return HttpResponseRedirect(f'http://127.0.0.1:8000/display_transaction/{lowaner[0].name}')

def display_transaction(request, name):
	transaction = Transaction.objects.filter()
	transaction = transaction[len(transaction) - 1]
	context = {'lowaner' : transaction.lowaner, 
				'debtor' : transaction.debtor,
				'mouny_moved' : transaction.mouny_moved,
				'resone' : transaction.resone,
				'date' : transaction.date}
	return render(request, 'debt_meneger/display_transaction.html', {'transaction' : context})	


def read_url_num(request, num):
	context = f'read_url_num  power {lib_power(num)}'
	return render(request, 'debt_meneger/context.html', {'context': context})

def roommate_data(request, name):
	data = Partner.objects.filter(name=name)
	partner_data = [data[0].name,
					data[0].date_of_berith,
					data[0].phone,
					data[0].email,]

	age = lib_age(data[0].date_of_berith)
	partner_data.append(age)
	context = {'context' : partner_data}
	return render(request, 'debt_meneger/context.html', context)
	
def update_phone_number(request, name, phone):
	partner = Partner.objects.get(name=name)
	partner.phone = phone
	partner.save()
	context = {'context' : partner.phone}	
	
	return render(request, 'debt_meneger/context.html', context)

def create_new_partner(request, name, date_of_berith, phone, email):
	new_partner = Partner(name, date_of_berith, phone, email)
	new_partner.save()
	return HttpResponseRedirect(f'http://127.0.0.1:8000/display_partner/{name}')

def delete_partner(request, name):
	Partner.objects.get(name=name).delete()
	context = {'context': f'{name} is removed from data base'}
	return render(request, 'debt_meneger/context.html', context)

def display_partner(request,name):
	partner = Partner.objects.get(name=name)
	context = {'name' : partner.name, 
			   'date_of_berith' : partner.date_of_berith,
			   'phone' : partner.phone,
			   'email' : partner.email,
			   'age' : lib_age(partner.date_of_berith)}
	return render(request, 'debt_meneger/display_partner.html', context)	

def display_all_partners(request):
	partners = Partner.objects.all()
	context = {'partners': partners}
	return render(request, 'debt_meneger/display_all_partners.html', context)

def add_partner(request):
	print('add_partner')
	if request.method == 'GET':
		return render(request, 'debt_meneger/add_partner.html')

	if request.method == 'POST':
		data = request.POST
		name = data['name']
		date_of_berith = data['date_of_berith']
		phone = data['phone']
		email =	 data['email']
		new_partner = Partner(name, date_of_berith, phone, email)	
		new_partner.save()
		return HttpResponseRedirect(f'http://127.0.0.1:8000/display_partner/{name}')

def display_partner_debt_sum(request):
	if request.method == 'GET':
		return render(request, 'debt_meneger/choose_partner.html')

	if request.method == 'POST':
		partner_name = request.POST['partenr']
		partner_lowns = Transaction.objects.filter(lowaner__name=partner_name)
		partner_lowns_mouny = [i.mouny_moved for i in partner_lowns]
		partner_debts = Transaction.objects.filter(debtor__name=partner_name)
		partner_debts_mouny = [i.mouny_moved for i in partner_debts]
		partner_total = subtract_lowns_from_debt(partner_lowns_mouny, partner_debts_mouny)
		context = {	'partner_name' : partner_name,
					'partner_debts' : partner_debts, 
					'partner_lowns' : partner_lowns, 
					'partner_total':partner_total}
		return render(request, 'debt_meneger/display_partner_debt_sum.html', context=context)

@api_view(['GET', 'POST'])
def transaction_list(request):
	if request.method == 'GET':
		data = Transaction.objects.all()
		serializer = TransactionSerializer(data, context={'request':request}, many=True)
		return Response(serializer.data)

	if request.method == 'POST':
		serializer = TransactionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'DELETE'])
def transaction_dtails(request):
	try:
		transaction = Transaction.objects.get(pk=10)
		print(f'transaction dtails: {transaction}')
	except transaction.DosNotExist:
		return Response(status=status.HTTP_404_NOT_FUOND)

	if request.method == 'PUT':
		serializer = TransactionSerializer(transaction, data=request.data, context={'request' : request})
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT) #not shure why 204 and not 

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		transaction.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def partner_details(request, pk):
	try:
		partner = Partner.objects.get(pk='bob@gmail.com')
		print(f'partner: {partner}, {type(partner)}')
		ser=PartnerSerializer(partner)
	
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		print(dir(status))
		return Response(status=status.HTTP_202_ACCEPTED)

	if request.method == 'PUT':
		serializer = PartnerSerializer(partner, data=request.data, context={'request' : request})
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT) #not shure why 204 and not 

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		partner.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



# def return_json(request):
# 	partner = Partner.objects.get(pk='bob@gmail.com')
# 	serializer = PartnerSerializer(partner)
# 	partner_json = serializer.data
# 	return Response(serializer.data)

# 	context = {'context': serializer.data}
# 	return render(request, 'debt_meneger/context.html', context)


# def return_json(request):
# 	if request.method == 'GET':
# 		data = Transaction.objects.all()
# 		serializer = TransactionSerializer(data, context={'request':request}, many=True)
# 		return Response(serializer.data)

class PartnerViewSet(viewsets.ViewSet):
	def list (self, request):
		queryset = Partner.objects.filter(name='bob')
		serializer = PartnerSerializer(queryset,context={'request':request} , many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		queryset = Partner.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		serializer = UserSerializer(usetr)
		return Response(serializer.data)



