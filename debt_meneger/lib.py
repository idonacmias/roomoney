from datetime import date

def subtract_lowns_from_debt(lowns, debt):
	sum_lowns = sum_list(lowns)
	sum_debt = sum_list(debt)
	return sum_lowns - sum_debt

def sum_list(transactions):
	sum_transaction = 0
	for transaction in transactions:
		sum_transaction += transaction

	return sum_transaction

def lib_power(num):
	return num ** 2

def lib_age(date_of_birth):
	today = date.today()
	age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.year))
	return age

def print_all(all_transaction):
	for transaction in all_transaction:
		print(transaction)		
