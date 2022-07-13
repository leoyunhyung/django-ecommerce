# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from ecommerce.apps.users.inlines import PointInline
from ecommerce.apps.users.models import User, UserSecession, UserAddress
from ecommerce.bases.admin import Admin


@admin.register(User)
class UserAdmin(Admin, UserAdmin):
    list_display = ('email', 'name', 'phone', 'point', 'auth_token', 'is_staff')
    search_fields = ('email', 'name', 'phone', 'point')
    list_filter = ()
    ordering = ('-created',)

    fieldsets = (
        ('User Profile', {'fields': ('id', 'email', 'password', 'point', 'auth_token')}),
        ('Authority', {'fields': ('is_staff',)}),
        ('Date', {'fields': ('created', 'modified')}),
    )

    add_fieldsets = (
        ('User Profile', {'fields': ('email', 'password1', 'password2')}),
        ('Authority', {'fields': ('is_staff',)}),
        ('Date', {'fields': ('created', 'modified',)}),
    )

    readonly_fields = ('auth_token', "created", "modified")
    inlines = (PointInline,)


@admin.register(UserSecession)
class UserSecessionAdmin(Admin):
    list_display = ('email', 'name', 'phone', 'reason')
    search_fields = ('email', 'name', 'phone', 'reason')
    list_filter = ()
    ordering = ()


# 기본 배송지 삭제 금지
@admin.register(UserAddress)
class UserAddressAdmin(Admin):
    list_display = ('user', 'name', 'phone', 'total_address', 'main_address', 'sub_address', 'postal_code', 'is_default')
    search_fields = ('user__email', 'name', 'phone', 'total_address', 'main_address', 'sub_address', 'postal_code', 'is_default')
    list_filter = ()
    ordering = ('-created',)

    fieldsets = (
        ("Fk", {"fields": ('user',)}),
        ("Main", {"fields": ('name', 'phone', 'main_address', 'sub_address', 'postal_code')}),
        ("Boolean", {"fields": ('is_default',)}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    add_fieldsets = (
        ("Fk", {"fields": ('user',)}),
        ("Main", {"fields": ('name', 'phone', 'main_address', 'sub_address', 'postal_code')}),
        ("Boolean", {"fields": ('is_default',)}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    readonly_fields = ("created", "modified")
