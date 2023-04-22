from django.contrib import admin
from .models import New, Comments, Contact


@admin.register(New)
class NewsModel(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ['create_time', 'status', ]


admin.site.register(Comments)
admin.site.register(Contact)
