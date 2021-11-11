from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import StudentUserSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


# @api_view(['GET', 'POST'])
# def api(request):
#     if request.method == "GET":
#         return Response({'msg': 'This is a GET request'})
#
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg': 'This is a POST request', 'data': request.data})


# FUNCTION BASED API VIEW

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            stu = StudentUser.objects.get(id=pk)
            serializer = StudentUserSerializer(stu)
            return Response(serializer.data)

        stu = StudentUser.objects.all()
        serializer = StudentUserSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        stu = StudentUser.objects.get(id=pk)
        serializer = StudentUserSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == "DELETE":
        stu = StudentUser.objects.get(id=pk)
        stu.delete()
        return Response({"msg": "data deleted"})
        return Response(serializer.errors)



        # Class BASED API VIEW


# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from .models import *
# from .serializer import StudentUserSerializer
# from rest_framework.views import API_VIEW
#
#
# class API(API_VIEW):
#     def get(self, request, pk=None, format=None):
#         if pk is not None:
#             stu = StudentUser.objects.get(id=pk)
#             serializer = StudentUserSerializer(stu)
#             return Response(serializer.data)
#
#         stu = StudentUser.objects.all()
#         serializer = StudentUserSerializer(stu, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         if request.method == "POST":
#             serializer = StudentUserSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"msg": "data created"}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def put(self, request,pk, format=None):
#         stu = StudentUser.objects.get(id=pk)
#         serializer = StudentUserSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "data updated"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#
#     def delete(self, request, pk, format=None):
#         stu = StudentUser.objects.get(id=pk)
#         stu.delete()
#         return Response({"msg": "data deleted"})
#         return Response(serializer.errors)

# urls.py
#
#     path('api', views.API.as_views()),
#     path('api/<int:pk>', views.API.as_views()),
