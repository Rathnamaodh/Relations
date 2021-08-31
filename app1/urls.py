from django.urls import path
from app1 import views


urlpatterns = [
   
    path('all', views.all_records_sql),
    path('create', views.create_sql), 
    path('update', views.update_sql), 
    path('delete', views.delete_sql),
]