from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('all',views.apiOverview,name="api-overview"),

    path('getuser/<email>',views.getUser,name="getuser"),
    path('createuser',views.createUser,name="createuser"),
    path('updateuser/<pk>',views.updateUser,name="updateuser"),
    path('deleteuser/<pk>',views.deleteUser,name="updateuser"),
    
]