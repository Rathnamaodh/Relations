from django.contrib import admin
# from mtm.models import Doctor,Patient

# # # Register your models here.

# # class DoctorModelAdmin(admin.ModelAdmin):
# #     list_display = ['id','doctor']

# # class PatientModelAdmin(admin.ModelAdmin):
# #     list_display = ['id','patient']

# # admin.site.register(Doctor,DoctorModelAdmin)
# # admin.site.register(Patient,PatientModelAdmin)

# admin.site.register(Doctor)
# admin.site.register(Patient)

from .models import Doctor,Patient

admin.site.register(Doctor)
admin.site.register(Patient)
