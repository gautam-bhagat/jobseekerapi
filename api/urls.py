from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('all',views.apiOverview,name="api-overview"),

    path('getuser/<email>',views.getUser,name="getuser"),
    path('createuser',views.createUser,name="createuser"),
    path('updateuser/<pk>',views.updateUser,name="updateuser"),
    path('deleteuser/<pk>',views.deleteUser,name="updateuser"),

    path('geteducation/<str:edu_id>',views.getEducation,name="geteducation"),
    path('geteducationsofuser/<str:user_id>',views.getEducationsOfUser,name="geteducationsofuser"),
    path('createeducation',views.createEducation,name="createeducation"),
    path('update-education/<str:edu_id>',views.updateEducation,name="updateeducation"),
    path('delete-education/<str:edu_id>',views.deleteEducation,name="deleteeducation"),
]