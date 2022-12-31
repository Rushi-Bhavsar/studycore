import datetime
import re
import pytz
import time

from django.core.management.base import BaseCommand
from django.conf import settings
from google_services.utils.google_api_wrapper import google_drive_service, google_sheets_service
import pandas as pd
from google_services.models import DailyAttendanceReport
SHEETS_PRE_FIX_NAME = 'SEM_1'


def get_session_details(value_range_0):
    row_data = []
    for value in value_range_0['values']:
        if value:
            row_data.append(value[0])
    return row_data


def create_payload(df):
    sheet_data = []
    for index, row in df.iterrows():
        data = {'subject_name': row['subject_name'], 'subject_short_name': row['subject_short_name'],
                'subject_code': row['subject_code'], 'session_mode': row['session_mode'],
                'class_room': row['class_room'], 'attendance_date': row['attendance_date'],
                'attendance_from_time': row['attendance_from_time'], 'attendance_to_time': row['attendance_to_time'],
                'faculty_initials': row['faculty_initials'], 'session_type': row['session_type'],
                'unit_no': row['unit_no'], 'topic_description': row['topic_description'],
                'daily_attendance_percentage': row['daily_attendance_percentage'], 'roll_no': row['roll_no'],
                'present_or_absent': row['present_or_absent'], 'roll_no_excused': row['roll_no_excused'],
                'roll_no_late': row['roll_no_late'], 'record_entry_time': row['record_entry_time']}
        sheet_data.append(data)
    return sheet_data


def save_to_database(payload_data):
    for payload in payload_data:
        created = DailyAttendanceReport.objects.create(**payload)


def get_entry_on(date_time_string):
    if len(date_time_string) == 16:
        date_time_string += ':00'
    try:
        entry_on_time = datetime.datetime.strptime(date_time_string, '%d/%m/%Y %H:%M:%S')
    except ValueError as v:
        print("Day Month Swap Done")
        entry_on_time = datetime.datetime.strptime(date_time_string, '%m/%d/%Y %H:%M:%S')

    # To avoid django native datetime warning, using timezone datetime.
    ist_time = pytz.timezone(settings.TIME_ZONE)
    entry_on_time = ist_time.localize(entry_on_time)
    return entry_on_time


class Command(BaseCommand):

    def __init__(self):
        self.sheet_ids = None
        super().__init__()

    def handle(self, *args, **options):
        t1 = time.time()
        self.delete_data()
        self.get_sheets_id_from_drive()
        self.get_sheets_data()
        t2 = time.time()
        self.stdout.write(f"Total Execution Time of batch job is: {int(t2-t1)} seconds.")

    def get_sheets_id_from_drive(self):
        drive_api = google_drive_service()
        folder_type = 'application/vnd.google-apps.folder'
        query_string = f"mimeType = '{folder_type}' and name = 'RKB' and trashed = false"
        driver_res = drive_api.files().list(q=query_string, fields='files(id, name)').execute()
        folder_ids = [item['id'] for item in driver_res['files']]
        query = f"parents='{folder_ids[0]}' and name contains '{SHEETS_PRE_FIX_NAME}' and trashed = false"
        folder_data = drive_api.files().list(q=query, fields='files(id, name)').execute()
        self.sheet_ids = [item['id'] for item in folder_data['files']]
        # self.stdout.write(f"Total Sheets under the folder: {len(self.sheet_ids)}")

    def get_sheets_data(self):
        for sheet_id in self.sheet_ids:
            # self.stdout.write(f"Processing sheet: '{sheet_id}'.")
            response = self.call_google_sheets_api_for_sheet(sheet_id)
            df = self.parse_google_sheets_data(response)
            payload_data = create_payload(df)
            save_to_database(payload_data)
            # self.stdout.write(f"Processing completed for sheet: '{sheet_id}'.")

    def call_google_sheets_api_for_sheet(self, sheet_id):
        range_sheet = ['Faculty!C2:C8', 'Report!B2:C', 'Report!E2:M', 'Report!P2:P']
        sheets_api = google_sheets_service()
        response = sheets_api.spreadsheets().values().batchGet(spreadsheetId=sheet_id, majorDimension='ROWS',
                                                               ranges=range_sheet).execute()
        return response

    def parse_google_sheets_data(self, response):
        valueRanges = response['valueRanges']
        columns = ['subject_name', 'subject_short_name', 'subject_code', 'session_mode', 'class_room',
                   'attendance_date', 'faculty_initials', 'attendance_from_time', 'attendance_to_time', 'session_type',
                   'unit_no', 'topic_description', 'present_or_absent', 'roll_no', 'roll_no_excused', 'roll_no_late',
                   'record_entry_time', 'daily_attendance_percentage']
        value_range_0 = dict(valueRanges[0])
        value_range_1 = dict(valueRanges[1])
        value_range_2 = dict(valueRanges[2])
        value_range_3 = dict(valueRanges[3])
        session_data = get_session_details(value_range_0)
        sheet_row = []
        for index, value in enumerate(zip(value_range_1['values'], value_range_2['values'], value_range_3['values'])):
            row_data = list(session_data)
            for item in value:
                row_data.extend(item)
            date_input_format = '%d/%m/%Y'
            string_date = str(row_data.pop(5))
            attendance_date = datetime.datetime.strptime(string_date, date_input_format).date()
            row_data.insert(5, attendance_date)

            string_time = str(row_data.pop(7))
            regex_time_pattern = r'[\d:\d]+'
            from_time, to_time = re.findall(regex_time_pattern, string_time)
            from_time = datetime.datetime.strptime(from_time, '%H:%M').time()
            to_time = datetime.datetime.strptime(to_time, '%H:%M').time()
            row_data.insert(7, from_time)
            row_data.insert(8, to_time)

            row_data[12] = False if row_data[12] == 'FALSE' else True
            entry_on_time = get_entry_on(row_data[-2])
            row_data[-2] = entry_on_time
            sheet_row.append(row_data)

        df = pd.DataFrame(sheet_row, columns=columns)
        return df

    def delete_data(self):
        DailyAttendanceReport.objects.all().delete()
        self.stdout.write(f"Delete all Records.")
