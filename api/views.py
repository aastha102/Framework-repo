from django.shortcuts import render
from django.http import JsonResponse
from .models import Student_API
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# # Create your views here.
# def StudentView(request):
#     students = Student_API.objects.all()
#     students_list = list(students.values())
#     return JsonResponse(students_list, safe= False)

@api_view(['GET', 'POST '])
def StudentView(request):
    if request.method == 'GET':
        
        students = Student_API.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status==status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, pk):
    try:
        student = Student_API.objects.get(pk=pk)
    except Student_API.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)