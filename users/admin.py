from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at',)

@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ('full_name', 'mobile_number', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'role')
    search_fields = ('full_name', 'mobile_number', 'email')
    ordering = ('-joining_date',)
    
    fieldsets = (
        (None, {'fields': ('mobile_number', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email', 'dob', 'address', 'profile_image')}),
        ('Employment', {'fields': ('joining_date', 'salary', 'role', 'documents')}),
        ('Bank Details', {'fields': ('bank_account',)}),
        ('Emergency Contact', {'fields': ('emergency_contact',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number', 'full_name', 'password1', 'password2'),
        }),
    )
