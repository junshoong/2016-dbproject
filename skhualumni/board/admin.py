from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at')
    search_fields = ('title', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
