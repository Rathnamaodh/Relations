from django.urls import path
from m2m import views


urlpatterns = [
    path('create',views.doctor),
    path('pc',views.patient),
    path('pd',views.patient_doctor),
]