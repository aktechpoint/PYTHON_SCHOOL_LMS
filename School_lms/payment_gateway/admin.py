from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payer_name', 'payer_email', 'amount', 'transaction_id', 'payment_date', 'status', 'method')
    search_fields = ('payer_name', 'payer_email', 'transaction_id')
    list_filter = ('status', 'method', 'payment_date')