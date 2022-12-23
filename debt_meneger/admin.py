from django.contrib import admin
from .models import Transaction, Partner




# Register your models here.



class TransactionAdmin(admin.ModelAdmin):
    pass



class PartnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Partner, PartnerAdmin)



