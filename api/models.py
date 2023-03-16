from django.db import models

# Create your models here.

class DEVICE(models.Model):
    MAC_ID = models.CharField(max_length=100, primary_key=True)
    AUTH_TOKEN = models.CharField(max_length=100)


class Users(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    skills = models.TextField(blank=True,null=True)
    profile_pic = models.TextField(default="null")
    banner_pic = models.TextField(default="null")
    github = models.CharField(max_length=100,default="null")
    leetcode = models.CharField(max_length=100,default="null")
    codechef = models.CharField(max_length=100,default="null")
    organization = models.CharField(max_length=100,default="0")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    grade = models.CharField(max_length=100,default= "null")
    start_date = models.DateField(max_length=100)
    end_date = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Experience(models.Model):
    exp_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)
    end_date = models.DateField(max_length=100,null=True)
    isWorking = models.CharField(default="False",max_length=100)
    # details = models.TextField(default="null")
    created_at = models.DateTimeField(auto_now_add=True)


class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile_pic = models.TextField(default="null")
    banner_pic = models.TextField(default="null")
    description = models.TextField(default="null")
    created_at = models.DateTimeField(auto_now_add=True)

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    key_skills = models.TextField(default="null")
    place = models.CharField(max_length=100)
    details = models.TextField(default="null")
    created_at = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    app_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)