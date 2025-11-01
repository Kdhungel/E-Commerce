from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = (
    'email', 'userName', 'fName', 'lName', 'lastLogin', 'dateJoined', 'is_active', 'is_staff', 'is_admin')

    # Make some fields readonly
    readonly_fields = ('password', 'dateJoined', 'lastLogin')
    search_fields = ('userName','email')  # Makes username searchable
    list_display_links = ('userName','email')  # Makes username clickable to open detail page

    # Fields for creating/editing users in admin
    fieldsets = (
        (None, {'fields': ('email', 'userName', 'fName', 'lName', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin')}),
        ('Important dates', {'fields': ('lastLogin', '-dateJoined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'userName', 'fName', 'lName', 'password1', 'password2', 'is_active', 'is_staff', 'is_admin',
            'is_superadmin')}
         ),
    )

    search_fields = ('email', 'userName', 'fName', 'lName')
    ordering = ('fName',)
    filter_horizontal = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)
