from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fields  = ('sid', 'fname', 'lname', 'tel', 'email')
    list_display  = ('sid', 'fname', 'lname', 'tel', 'userId')
    search_fields = ('sid', 'fname', 'lname', 'email')

admin.site.register(Student, StudentAdmin)
