from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users

@api_view(['GET'])
def apiOverview(request):
    urls ={

        'Get User' : '/getuser/<email>',
        'Create User' : '/createuser/',
        'update User':'updateuser/<pk>',
        'delete user':'deleteuser/<pk>',
    }

    return Response(urls)


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