# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from ecommerce.apps.users.models import User, UserSecession
from ecommerce.bases.admin import Admin


@admin.register(User)
class UserAdmin(Admin, UserAdmin):
    list_display = ('email', 'name', 'phone', 'auth_token', 'is_staff')
    search_fields = ('email', 'name', 'phone')
    list_filter = ()
    ordering = ('-created',)

    fieldsets = (
        ('User Profile', {'fields': ('id', 'email', 'password', 'auth_token')}),
        ('Authority', {'fields': ('is_staff',)}),
        ('Date', {'fields': ('created', 'modified')}),
    )

    add_fieldsets = (
        ('User Profile', {'fields': ('email', 'password1', 'password2')}),
        ('Authority', {'fields': ('is_staff',)}),
        ('Date', {'fields': ('created', 'modified',)}),
    )

    readonly_fields = ('auth_token', "created", "modified")


@admin.register(UserSecession)
class UserSecessionAdmin(Admin):
    list_display = ('email', 'name', 'phone', 'reason')
    search_fields = ('email', 'name', 'phone', 'reason')
    list_filter = ()
    ordering = ()
