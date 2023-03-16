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

    path('getexperience/<str:exp_id>',views.getExperience,name="getexperience"),
    path('getexperiencesofuser/<str:user_id>',views.getExperiencesOfUser,name="getexperiencesofuser"),
    path('createexperience',views.createExperience,name="createexperience"),
    path('update-experience/<str:exp_id>',views.updateExperience,name="updateexperience"),
    path('delete-experience/<str:exp_id>',views.deleteExperience,name="deleteexperience"),

    path('getpage/<str:page_id>',views.getPage,name="getpage"),
    path('getpagesofuser/<str:user_id>',views.getPagesOfUser,name="getpagesofuser"),
    path('createpage',views.createPage,name="createpage"),
    path('update-page/<str:page_id>',views.updatePage,name="updatepage"),
    path('delete-page/<str:page_id>',views.deletePage,name="deletepage"),

    path('getalljobs',views.getJobsOfUser,name="getalljobs"),
    path('getjob/<str:job_id>',views.getJob,name="getjob"),
    path('createjob',views.createJob,name="createjob"),
    path('update-job/<str:job_id>',views.updateJob,name="updatejob"),
    path('delete-job/<str:job_id>',views.deleteJob,name="deletejob"),

    path('getallapplications',views.getApplicationsOfUser,name="getallapplications"),
    path('getapplication/<str:app_id>',views.getApplication,name="getapplication"),
    path('createapplication',views.createApplication,name="createapplication"),
    path('update-application/<str:app_id>',views.updateApplication,name="updateapplication"),
    path('delete-application/<str:app_id>',views.deleteApplication,name="deleteapplication"),

    path('adddevice/<str:mac_id>',views.addDevice,name="adddevice"),
]