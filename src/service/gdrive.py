import os
from google.oauth2 import service_account
from googleapiclient.discovery import build, Resource

from icecream import ic

class Gdrive:
    def __init__(self) -> None:

        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.SERVICE_ACCOUNT_FILE = "src/credentials/pygdrive-414404-6f97193be94d.json"

        self.credentials = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.drive_service: Resource = build('drive', 'v3', credentials=self.credentials)

        ic(type(self.credentials))
        ...

    def create_folder(self, path: str= None) -> str:

        folder_id = 'root'
        folders = 'data_eheheheh'
        # for folder in folders:

        service = build("drive", "v3", credentials=self.credentials)
        folder_metadata = {
            'name': 'folder_name',
            "parents": ['1Z6tJEWLjISTZDX0fRRpipAB_96E98TfM'],
            'mimeType': 'application/vnd.google-apps.folder'
        }

        new_folder = service.files().create(body=folder_metadata).execute()
        ic(new_folder)

            
        ...

    def main(self, base_path: str) -> None:
        self.create_folder()
        # ic(self.drive_service)
        # for root, dirs, files in os.walk(base_path):
        #     for file in files:
        #         file_path = os.path.join(root, file).replace('\\', '/')
        #         ic(root)
        #         ic(file_path)

