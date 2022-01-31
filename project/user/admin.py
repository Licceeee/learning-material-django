from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ['last_login', 'date_joined',
                       'is_superuser']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'email', 'first_name', 'last_name', 'last_login',
                    'get_groups', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_active',)
    # when edit existing user
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name',
                           'is_superuser', 'headshot_image',
                           'date_joined', 'last_login',  'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1',
                       'password2', 'is_staff', 'is_active',
                       'date_joined', 'last_login', 'is_superuser',)
            }),
        )
    ordering = ('email',)
