# Generated by Django 4.1.4 on 2022-12-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_short_name', models.CharField(max_length=10)),
                ('subject_code', models.PositiveIntegerField()),
                ('session_mode', models.CharField(max_length=2)),
                ('class_room', models.CharField(max_length=5)),
                ('attendance_date', models.DateField()),
                ('faculty_initials', models.CharField(max_length=10)),
                ('attendance_from_time', models.TimeField()),
                ('attendance_to_time', models.TimeField()),
                ('session_type', models.CharField(max_length=15)),
                ('unit_no', models.PositiveSmallIntegerField()),
                ('topic_description', models.TextField()),
                ('present_or_absent', models.BooleanField()),
                ('roll_no', models.CharField(max_length=200)),
                ('roll_no_excused', models.CharField(blank=True, max_length=200, null=True)),
                ('roll_no_late', models.CharField(blank=True, max_length=200, null=True)),
                ('record_entry_time', models.DateTimeField()),
                ('daily_attendance_percentage', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DriveApiDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SheetsApiDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
