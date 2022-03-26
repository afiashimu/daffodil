from django.contrib import admin
from .models import student_info
# Register your models here.
@admin.register(student_info)

class UserAdmin(admin.ModelAdmin):
    list_display=['student_id','student_name','student_dept','sec','email','phone_number']