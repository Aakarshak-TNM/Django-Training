from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Students model should have following fields (name, rollno, standard, course)
# The standard model should have following fields (standard_name) rest you can add up on your own
# The student table should have this standard field as foreign key


class Standard(models.Model):
    standard_name = models.CharField(max_length=10)

    def __str__(self):
        return f"Standard Name: {self.standard_name}"


class Student(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    standard = models.CharField(max_length=10)
    course = models.CharField(max_length=20)
    standard_name = models.ForeignKey(
        Standard, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.rollno}, Standard: {self.standard}, Course: {self.course}, {self.standard_name}"
