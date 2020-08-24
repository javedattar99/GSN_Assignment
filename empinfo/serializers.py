


from rest_framework import serializers
from empinfo.models import Employee,Project,Employeeproject



class EmployeeSerializers(serializers.ModelSerializer):
    p_manager = serializers.SerializerMethodField()
    report_manager = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = ('first_name','last_name','email','date_joined','is_active','p_manager','report_manager')


    @staticmethod
    def get_report_manager(obj):
        print(id(obj))
        report_manager = obj.report_manager
        data = {}
        if report_manager:
            data['first_name'] = report_manager.first_name
        return data

    @staticmethod
    def get_p_manager(obj):
        print(id(obj))
        manager_data = []
        for project_employee in obj.project_employee.select_related():
            project_manager=project_employee.project.project_manager
            data = {}
            data['first_name'] = project_manager.first_name
            data['project_title'] = project_employee.project.title
            data['project_desc'] = project_employee.project.description
            manager_data.append(data)
        return manager_data


class ProjectSerializer(serializers.ModelSerializer):
    project_manager = serializers.StringRelatedField(read_only=True)
    employee = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ('title','description','start_date','end_date','is_active','project_manager','employee')


    @staticmethod
    def get_employee(obj):
        employee_data = []
        for project_employee in obj.project_main.select_related():
            data = {}
            data['first_name'] = project_employee.employee.first_name
            employee_data.append(data)
        return employee_data


class EmployeeProjectSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True, many=True)
    employee = serializers.StringRelatedField(read_only=True,many=True)

    class Meta:
        model = Employeeproject
        fields = "__all__"

