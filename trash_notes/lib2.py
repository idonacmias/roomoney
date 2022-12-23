'''transaction hendler module'''


def new_transaction(data, transactions):
	transaction = {
		'lowaner' : data[0],
		'debtor' : data[1],
		'mouny_moved' : data[2],
		'resone' : data[3],
		'date' : data[4],
	}
	transactions.append(transaction)

def print_transaction(transaction):
	print(f"{transaction['lowaner']} loan to {transaction['debtor']} {transaction['mouny_moved']} shekels for {transaction['resone']} in {transaction['date']}")

def print_all(transactions):
	for transaction in transactions:
		print_transaction(transaction)		

def sum_debt(transactions):
	res_debt = {}
	for transaction in transactions:
		if transaction['lowaner'] in res_debt.keys():
			res_debt[transaction['lowaner']] += int(transaction['mouny_moved'])

		else: 
			res_debt.update({transaction['lowaner'] : int(transaction['mouny_moved'])})

		if transaction['debtor'] in res_debt.keys():
			res_debt[transaction['debtor']] -= int(transaction['mouny_moved'])

		else:
			res_debt.update({transaction['debtor'] : int(transaction['mouny_moved']) * -1})

	return res_debt

if __name__ == '__main__':
	transactions = []
	data = 'saly' ,'bob','50','shoping','2020-11-21'
	new_transaction(data, transactions)
	data = 'bob', 'saly', '25', 'food', '2020-11-21'
	new_transaction(data, transactions)
	data = 'saly' ,'bob','5','shoping','2020-11-21'
	new_transaction(data, transactions)
	data = 'mark', 'snail', '80', 'salt', '2022-11-21'
	new_transaction(data, transactions)
	print_all(transactions)
	print(sum_debt(transactions))
