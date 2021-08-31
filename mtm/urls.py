from django.urls import path
from mtm import views


urlpatterns = [
    path('create',views.doctor),
    # path('pc',views.Project_create),
]