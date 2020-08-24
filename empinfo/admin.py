from django.contrib import admin
from .models import Employee,Project,Employeeproject
# Register your models here.


admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Employeeproject)