from rest_framework import serializers
from .models import Transaction, Partner

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction 
        fields = ('pk', 'lowaner', 'debtor', 'mouny_moved', 'resone', 'date')

class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('pk','name', 'date_of_berith', 'phone', 'email')


