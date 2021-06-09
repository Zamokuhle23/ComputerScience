from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=30)

class Employee(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_description = models.CharField(max_length=30)
    age = models.IntegerField()

class Head_of_department(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class CEO(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Company(models.Model):
    company_name = models.CharField(max_length=30)
    ceo = models.ForeignKey(CEO, on_delete=models.CASCADE)
    Company_description = models.TextField()





