from django.contrib import admin
from .models import StudentInfo


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'address']


admin.site.register(StudentInfo, StudentAdmin)
