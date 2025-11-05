from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'first_name', 'last_name',
        'last_login', 'date_joined', 'is_active', 'is_staff', 'is_admin'
    )
    list_display_links = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('first_name',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_super_admin')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name',
                'password1', 'password2', 'is_active', 'is_staff', 'is_admin', 'is_super_admin'
            ),
        }),
    )

    filter_horizontal = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)
