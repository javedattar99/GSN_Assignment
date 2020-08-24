from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    report_manager = models.ForeignKey('self', null=True, related_name = 'reporting_manager',blank=True,on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (self.first_name+ ' ' + self.last_name)


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    # employee = models.ManyToManyField(Employee)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='p_manager')

    def __str__(self):
        return self.title


class Employeeproject(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='project_employee')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_main')


    def __str__(self):
        return self.project.title