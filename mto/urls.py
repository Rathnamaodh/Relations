from django.urls import path
from mto import views


urlpatterns = [
    path('create',views.student_create),
    path('pc',views.Project_create),
]