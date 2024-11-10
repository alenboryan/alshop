from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from .models import ForMan, ForWoman

@admin.register(ForMan)
class ForManAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('category',)

@admin.register(ForWoman)
class ForWomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('category',)
