from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('login_id', 'name', 'email')
    search_fields = ('login_id', 'name', 'email')

admin.site.register(User, UserAdmin)
