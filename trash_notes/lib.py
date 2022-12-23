class Transaction:
	all_transaction = []

	def __init__(self, data):
		self.lowaner = data[0]
		self.debtor = data[1]
		self.mouny_moved = data[2]
		self.resone = data[3]
		self.date = data[4]
		Transaction.all_transaction.append(self)

	def __str__(self):
		return f'{self.lowaner} loan to {self.debtor} {self.mouny_moved} shekels for {self.resone} in {self.date}'

	def print_all():
		for transaction in Transaction.all_transaction:
			print(transaction)		

	def sum_debt():
		my_dict = {}
		for transaction in Transaction.all_transaction:
			if transaction.lowaner in my_dict.keys():
				my_dict[transaction.lowaner] += int(transaction.mouny_moved)

			else: 
				my_dict.update({transaction.lowaner : int(transaction.mouny_moved)})

			if transaction.debtor in my_dict.keys():
				my_dict[transaction.debtor] -= int(transaction.mouny_moved)

			else:
				my_dict.update({transaction.debtor : int(transaction.mouny_moved) * -1})

		return my_dict

if __name__ == '__main__':
	data = 'saly' ,'bob','50','shoping','2020-11-21'
	Transaction(data)
	data = 'bob', 'saly', '25', 'food', '2020-11-21'
	Transaction(data)
	data = 'saly' ,'bob','5','shoping','2020-11-21'
	Transaction(data)
	data = 'mark', 'snail', '80', 'salt', '2022-11-21'
	Transaction(data)
	Transaction.print_all()
	print(Transaction.sum_debt())
