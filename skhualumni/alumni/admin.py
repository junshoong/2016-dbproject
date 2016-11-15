from django.contrib import admin
from alumni.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'login_id')

admin.site.register(User, UserAdmin)

