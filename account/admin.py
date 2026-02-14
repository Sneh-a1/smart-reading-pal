from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
	model = User
	list_display = ("email", "is_staff", "is_active")
	list_filter = ("is_staff", "is_active")
	ordering = ("email",)
	search_fields = ("email", "name")
	fieldsets = (
		(None, {"fields": ("email", "password")}),
		("Profile", {"fields": ("name", "city")}),
		("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
		("Important dates", {"fields": ("last_login",)}),
	)
	add_fieldsets = (
		(None, {
			"classes": ("wide",),
			"fields": ("email", "password1", "password2", "is_staff", "is_active"),
		}),
	)

