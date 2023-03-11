from django.contrib import admin
from . import models
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','state','city','country','pincode','phone','github','leetcode','codechef','profile_pic','banner_pic','created_at')

admin.site.register(models.Users,UserAdmin)