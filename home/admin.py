from django.contrib import admin

# Register your models here.
from home.models import Student, Standard

admin.site.register(Student)
admin.site.register(Standard)
