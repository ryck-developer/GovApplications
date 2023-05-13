from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from app import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)})
    )
    list_display = [
        'email',
        'is_staff',
        'is_superuser',
        'is_active',
    ]
    search_fields = [
        'email'
    ]
    ordering = [
        'email'
    ]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'name'
    ]
    search_fields = [
        'user__username'
    ]
    autocomplete_fields = [
        'user'
    ]

@admin.register(models.AllCookies)
class AllCookiesAdmin(admin.ModelAdmin):
    list_display = [
        'cookie',
        'created_at'
    ]
