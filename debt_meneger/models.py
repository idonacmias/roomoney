from django.db import models

# Create your models here.



class Partner(models.Model):
	name = models.CharField(max_length=30)
	date_of_berith = models.DateField()
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=30, primary_key=True)

	def __str__(self):
		return self.name 

class Transaction(models.Model):
	lowaner = models.ForeignKey('Partner', related_name='lowaner', on_delete=models.PROTECT)
	debtor = models.ForeignKey('Partner', related_name='debtor', on_delete=models.PROTECT)
	mouny_moved = models.IntegerField()
	resone = models.CharField(max_length=60)
	date = models.DateField()

	def __str__(self):
		return f'{self.lowaner} to {self.debtor} bcouse {self.resone}'



