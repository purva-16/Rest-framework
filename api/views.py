from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List':'/task-list',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',

    }


    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    Serializer = TaskSerializer(tasks, many=True)

    return Response(Serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    Serializer = TaskSerializer(tasks, many=False)

    return Response(Serializer.data)

@api_view(['POST'])
def taskCreate(request):
    Serializer = TaskSerializer(data=request.data)

    if Serializer.is_valid():
        Serializer.save()


    return Response(Serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    Serializer = TaskSerializer(instance=task, data=request.data)

    if Serializer.is_valid():
        Serializer.save()


    return Response(Serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
   
    return Response(".")


