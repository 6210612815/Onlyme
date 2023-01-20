from django.contrib import admin
from .models import Equipment

# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    fields  = ('eid', 'name', 'desc', 'cat', 'image')
    list_display  = ('id','eid', 'name', 'cat')
    search_fields = ('eid', 'name', 'cat')

admin.site.register(Equipment, EquipmentAdmin)
