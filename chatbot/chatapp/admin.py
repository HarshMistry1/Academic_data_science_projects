from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import chatdata,chat

# Register your models here.
class data(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name', 'msg', 'reply']
    list_filter=['name', 'msg']

admin.site.register(chatdata, data)
admin.site.register(chat)