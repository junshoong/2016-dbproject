from django.contrib import admin
from info.models import Info


class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_date')
    search_fields = ('title',)

admin.site.register(Info, InfoAdmin)
