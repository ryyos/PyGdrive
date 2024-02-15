import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

class Gdrive:
    def __init__(self) -> None:

        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.SERVICE_ACCOUNT_FILE = "src/credentials/pygdrive-414404-6f97193be94d.json"

        self.credentials = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.drive_service = build('drive', 'v3', credentials=self.credentials)
        ...

    def create_folder(self, path: str) -> str:
        
        ...