from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
import secrets


def generate_token():
    return secrets.token_urlsafe(32)


# ------------------------------URLS--------------------------------------------
@api_view(['GET'])
def apiOverview(request):
    urls ={
        'API Overview' : 'add api/ before all the urls' ,
        'Get User' : '/getuser/<email>',
        'Create User' : 'createuser/',
        'update User':'updateuser/<pk>',
        'delete user':'deleteuser/<pk>',
        'Get Education':'geteducation/<edu_id>',

        'Get Educations of User':'geteducationsofuser/<user_id>',
        'get education' : 'geteducation/<edu_id>',
        'Create Education':'createeducation/',
        'Update Education':'update-education/<edu_id>',
        'Delete Education':'delete-education/<edu_id>',

        'Get Experience of User':'getexperiencesofuser/<user_id>',
        'get experience' : 'getexperience/<exp_id>',
        'Create Experience':'createexpereince/',
        'Update Expereince':'update-experience/<exp_id>',
        'Delete Experince':'delete-experience/<edu_id>',

        'Get Page of User':'getpagesofuser/<user_id>',
        'get page' : 'getpage/<page_id>',
        'Create Page':'createpage/',
        'Update Page':'update-page/<page_id>',
        'Delete Page':'delete-page/<page_id>',

        'Get All Pages':'getallpages/<user_id>',
        

    }

    return Response(urls)

# -------------------- USER ----------------------
@api_view(['GET'])
def getUser(request,email):
    users = Users.objects.get(email=email)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateUser(request,pk):
    user = Users.objects.get(user_id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request,pk):
    user = Users.objects.get(user_id=pk)
    user.delete()

    return Response({"Deleted": True})



# ----------------------------------Education -----------------------------------------
@api_view(['GET'])
def getEducationsOfUser(request,user_id):
    print(type(int(user_id)))
    # educations = Education.objects.all()
    educations = Education.objects.filter(user_id=user_id)
    serializer = EducationSerializer(educations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEducation(request,edu_id):
    education = Education.objects.get(edu_id=edu_id)
    serializer = EducationSerializer(education, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createEducation(request):
    serializer = EducationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateEducation(request,edu_id):
    education = Education.objects.get(edu_id=edu_id)
    serializer = EducationSerializer(instance=education, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEducation(request,edu_id):
    user = Education.objects.get(edu_id=edu_id)
    user.delete()

    return Response({"Deleted": True})


# --------------------------Experience--------------------------------------------
@api_view(['GET'])
def getExperiencesOfUser(request,user_id):
    experiences = Experience.objects.filter(user_id=user_id)
    serializer = ExperienceSerializer(experiences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getExperience(request,exp_id):
    experience = Experience.objects.get(exp_id=exp_id)
    serializer = ExperienceSerializer(experience, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createExperience(request):
    serializer = ExperienceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateExperience(request,exp_id):
    experience = Experience.objects.get(exp_id=exp_id)
    serializer = ExperienceSerializer(instance=experience, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteExperience(request,exp_id):
    experience = Experience.objects.get(exp_id=exp_id)
    experience.delete()

    return Response({"Deleted": True})


# --------------------------Page--------------------------------------------
@api_view(['GET'])
def getPagesOfUser(request,user_id):
    pages = Page.objects.filter(user_id=user_id)
    serializer = PageSerializer(pages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPage(request,page_id):
    page = Page.objects.get(page_id=page_id)
    serializer = PageSerializer(page, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPage(request):
    serializer = PageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updatePage(request,page_id):
    page = Page.objects.get(page_id=page_id)
    serializer = PageSerializer(instance=page, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePage(request,page_id):
    page = Page.objects.get(page_id=page_id)
    page.delete()

    return Response({"Deleted": True})

# ---------------------------------Job----------------------------
@api_view(['GET'])
def getJobsOfUser(request,user_id):
    jobs = Job.objects.filter(user_id=user_id)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getJob(request,job_id):
    job = Job.objects.get(job_id=job_id)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createJob(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateJob(request,job_id):
    job = Job.objects.get(job_id=job_id)
    serializer = JobSerializer(instance=job, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteJob(request,job_id):
    job = Job.objects.get(job_id=job_id)
    job.delete()

    return Response({"Deleted": True})

# ------------------------------Application-------------------------------
@api_view(['GET'])
def getApplicationsOfUser(request,user_id):
    applications = Application.objects.filter(user_id=user_id)
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getApplication(request,app_id):
    application = Application.objects.get(app_id=app_id)
    serializer = ApplicationSerializer(application, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createApplication(request):
    serializer = ApplicationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateApplication(request,app_id):
    application = Application.objects.get(app_id=app_id)
    serializer = ApplicationSerializer(instance=application, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteApplication(request,app_id):
    application = Application.objects.get(app_id=app_id)
    application.delete()

    return Response({"Deleted": True})


@api_view(['POST'])
def addDevice(request, mac_id):
    
    token = generate_token()

    exist = DEVICE.objects.filter(MAC_ID=mac_id).count()
    print(exist)
    if exist:
        device = DEVICE.objects.get(MAC_ID=mac_id)
        device.AUTH_TOKEN = token
        device.save()
        return Response({"AUTH_TOKEN":token })
    else:
        DEVICE(MAC_ID=mac_id, AUTH_TOKEN=token).save()
        return Response({"AUTH_TOKEN": token})

import numpy as np

def getindices(userskill,companyskill):
    ind = set()
    for i in userskill:
        print(i)
        for j in companyskill:
            if i in j:
                print("in jjj")
                print(companyskill.index(j))
                ind.add(companyskill.index(j))
    
    return list(ind)


@api_view(['GET'])
def getRecommendations(request, user_id):
    user = Users.objects.get(user_id=user_id)
    userskill =  user.skills
    userskill = userskill.split("|")
    userskill = [i.strip().lower() for i in userskill]

    jobs = Job.objects.all()
    jobs = np.array(list(jobs.values()))
    companyskills = [i.get("key_skills") for i in jobs]
    companyskills = [ i.split("|") for i in companyskills ]
    companyskills = [ [j.strip().lower() for j in i] for i in companyskills ]
    
    print(companyskills)
    ind = getindices(userskill,companyskills)
    print(ind)
    recommend = jobs[ind]
    return Response(recommend)

@api_view(['POST'])
def newRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def newTeam(request):
    serializer = TeamSerializer(data=request.data)
    saved = 0
    if serializer.is_valid():
        saved = 1
        serializer.save()
    return Response({"created": saved})

@api_view(['GET'])
def allRoom(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)