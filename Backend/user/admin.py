from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'nivel_entrenamiento', 'objetivo', 'is_staff']
    search_fields = ['email', 'username']