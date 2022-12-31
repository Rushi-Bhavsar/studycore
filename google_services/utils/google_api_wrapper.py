from .google_api_caller import GoogleAPIService


def google_sheets_service():
    google_service_api = GoogleAPIService('sheets', 'v4', ['https://www.googleapis.com/auth/spreadsheets'])
    service_api = google_service_api.create_service()
    return service_api


def google_drive_service():
    google_service_api = GoogleAPIService('drive', 'v3', ['https://www.googleapis.com/auth/drive'])
    service_api = google_service_api.create_service()
    return service_api

