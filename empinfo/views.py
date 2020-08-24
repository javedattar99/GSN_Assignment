


from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee,Project,Employeeproject
from .serializers import EmployeeSerializers,ProjectSerializer,EmployeeProjectSerializer
# Create your views here.


class EmployeeListView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class ProjectListView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# class EmployeeProjectListView(viewsets.ModelViewSet):
#     queryset = Employeeproject.objects.all()
#     serializer_class = EmployeeProjectSerializer