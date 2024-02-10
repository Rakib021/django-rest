from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)

class AdminStudent(admin.ModelAdmin):
  list_display =['id','name','city']
