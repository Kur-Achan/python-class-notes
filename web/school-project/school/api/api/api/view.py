from django.shortcuts import render
# from  restframework import serializer

from restframework.response import Response
from restframework view import APIView
from student.models import Student
from .serializer import  StudentSerializer

class StudentListView(APIView):

     def get(self, request):
        student=Student.object.all()
        serializer=StudentSerializer(students,may=True)

        return Response(serializer.data)
# Create your views here.
