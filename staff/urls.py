from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('', views.home , name='home'),
    path('insert/', views.insert, name='insert_data'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('update_details/<id>/', views.update, name='update_details'),
    path('delete/<id>/', views.delete, name='delete'),
]