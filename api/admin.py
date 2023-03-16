from django.contrib import admin
from . import models
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','state','city','country','phone','github','leetcode','codechef','profile_pic','banner_pic','created_at')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('edu_id' ,'user_id' ,'school' ,'degree' ,'field_of_study' ,'grade' ,'start_date' ,'end_date' ,'created_at')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('exp_id' ,'user_id' ,'company' ,'position' ,'start_date' ,'end_date'  ,'created_at')


admin.site.register(models.Users,UserAdmin)
admin.site.register(models.Education,EducationAdmin)
admin.site.register(models.Experience,ExperienceAdmin)
admin.site.register(models.Page)
admin.site.register(models.Job)
admin.site.register(models.Application)
admin.site.register(models.DEVICE)