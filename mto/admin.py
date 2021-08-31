from django.contrib import admin
from mto.models import Student,Project

# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','student']

admin.site.register(Student,StudentModelAdmin)
admin.site.register(Project,ProjectModelAdmin)

