# Django
from django.contrib import admin

# Local
from ecommerce.apps.banks.models import BankAccount
from ecommerce.bases.admin import Admin


@admin.register(BankAccount)
class BankAccountAdmin(Admin):
    list_display = ('user', 'bank', 'account', 'name')
    search_fields = ('user__email', 'bank', 'account', 'name')
    ordering = ('-created',)
    list_filter = ()

    fieldsets = (
        ("Fk", {"fields": ('user',)}),
        ("Main", {"fields": ('id', 'bank', 'account', 'name')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    add_fieldsets = (
        ("Fk", {"fields": ('user',)}),
        ("Main", {"fields": ('id', 'bank', 'account', 'name')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    readonly_fields = ("created", "modified")
