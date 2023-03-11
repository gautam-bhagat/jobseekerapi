from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET'])
def apiOverview(request):
    urls ={

        'Get User' : '/getuser/<email>',
        'Create User' : '/createuser/',
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

    return Response({"User Deleted": True})



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

    return Response({"User Deleted": True})


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

    return Response({"User Deleted": True})