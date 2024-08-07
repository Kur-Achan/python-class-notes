
from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.views import APIView
from  student.models import Student
from classroom.models import Classroom
# from class.models  import Class
from teacher.models import Teacher
from course.models import Course
from .serializers import  StudentSerializer
from.serializers import ClassroomSerializer
from.serializers import ClassSerializer
from .serializers import  TeacherSerializer
from .serializers import CourseSerializer

class StudentListView(APIView):
    def get(self,request):
        student=Student.objects.all
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
class ClassroomListView(APIView):
    def get(self,request):
        classroom=Classroom.objectseacherserializers.all
        serializer=ClassroomSerializer(classroom,many=True)
        return Response(serializer.data)
class ClassListView(APIView):
    def get(self,request):
        class=Class.objects.all
        serializer=ClassSerializer(class,many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all
        serializer= TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self,request):
        course=Course.objects.all
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data)
