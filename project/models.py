from django.db import models

# Create your models here.
class student_info(models .Model):
    student_id= models.IntegerField()
    student_name = models.CharField(max_length=20)
    student_dept = models.CharField(max_length=15)
    sec = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)