import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from django.conf import settings

CLIENT_SECRET_FILE = settings.CLIENT_SECRET_FILE
TOKEN_FILE = settings.TOKEN_FILE


class GoogleAPIService:
    def __init__(self, api_service_name: str, api_version: str, api_scopes: list):
        self.__client_secret_file = CLIENT_SECRET_FILE
        self.__api_service_name = api_service_name
        self.__api_scopes = api_scopes
        self.__api_version = api_version
        self.__token_file = self.__create_token_file()

    def create_service(self):
        creds = self.__create_cred()
        try:
            service = build(self.__api_service_name, self.__api_version, credentials=creds)
        except Exception as e:
            print(f"Error While creating Service: {e}")
            service = None
        return service

    def __create_cred(self):
        creds = None
        if os.path.exists(self.__token_file):
            creds = Credentials.from_authorized_user_file(self.__token_file, self.__api_scopes)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.__client_secret_file, self.__api_scopes)
                creds = flow.run_local_server(port=0)
            with open(self.__token_file, 'w') as token:
                token.write(creds.to_json())
        return creds

    def __create_token_file(self):
        service_token_file = self.__api_service_name + '_token.json'
        return os.path.join(TOKEN_FILE, service_token_file)
