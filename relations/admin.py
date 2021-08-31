from django.contrib import admin
from relations.models import Student,Student_Profile

# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']

class StudentProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','student','roll']

admin.site.register(Student,StudentModelAdmin)
admin.site.register(Student_Profile,StudentProfileModelAdmin)
