from django.urls import path
from relations import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('create', views.student_create),
    path('update',views.student_update),
    path('delete',views.student_delete),

    path('sp',views.student_profile_create),
]