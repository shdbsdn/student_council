from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'image')
    search_fields = ('title',)
    fields = ('title', 'content', 'image')

admin.site.register(Notice, NoticeAdmin)
