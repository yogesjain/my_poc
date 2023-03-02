from django.db import models

class Employee(models.Model):
  firstname = models.CharField(max_length=255)
  emp_id=models.IntegerField()