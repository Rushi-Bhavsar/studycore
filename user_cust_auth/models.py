from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=20)

