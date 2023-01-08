from django.db import models


class DailyAttendanceReport(models.Model):

    subject_name = models.CharField(max_length=50, blank=False, null=False)
    subject_short_name = models.CharField(max_length=10, blank=False, null=False)
    subject_code = models.PositiveIntegerField(blank=False, null=False)
    session_mode = models.CharField(max_length=2, blank=False, null=False)
    class_room = models.CharField(max_length=5, blank=False, null=False)
    attendance_date = models.DateField(blank=False, null=False)
    faculty_initials = models.CharField(max_length=10, blank=False, null=False)
    attendance_from_time = models.TimeField(blank=False, null=False)
    attendance_to_time = models.TimeField(blank=False, null=False)
    session_type = models.CharField(max_length=15, blank=False, null=False)
    unit_no = models.PositiveSmallIntegerField(blank=False, null=False)
    topic_description = models.TextField(blank=False, null=False)
    present_or_absent = models.BooleanField(blank=False, null=False)
    roll_no = models.CharField(max_length=200, blank=False, null=False)
    roll_no_excused = models.CharField(max_length=200, blank=True, null=True)
    roll_no_late = models.CharField(max_length=200, blank=True, null=True)
    record_entry_date = models.DateField(blank=False, null=False)
    daily_attendance_percentage = models.PositiveSmallIntegerField(blank=False, null=False)


class DriveApiDetails(models.Model):
    pass


class SheetsApiDetails(models.Model):
    pass
from django.db import models

# Create your models here.
