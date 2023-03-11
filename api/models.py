from django.db import models

# Create your models here.
class Users(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    profile_pic = models.TextField(default="null")
    banner_pic = models.TextField(default="null")
    github = models.CharField(max_length=100,default="null")
    leetcode = models.CharField(max_length=100,default="null")
    codechef = models.CharField(max_length=100,default="null")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


