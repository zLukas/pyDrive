import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from os import environ


class DriveLogin():
    def __init__(self) -> None:
        # If modifying these scopes, delete the file token.json.
        self.__scopes = ['https://www.googleapis.com/auth/drive.file',
                         'https://www.googleapis.com/auth/drive.readonly',
                         'https://www.googleapis.com/auth/drive.metadata',
                         'https://www.googleapis.com/auth/drive.metadata.readonly']
        # TODO: read token and creds dirs form env variables, validate them

    def validate_creds(self, creds):
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'pyDrive.json', self.__scopes)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())
        else:
            pass
        return creds

# TODO: Pass SCOPES and token as param
    def api_login(self):
        creds = None

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.__scopes)
        else:
            pass
        validated_creds = self.validate_creds(creds)

    
        service = build('drive', 'v3', credentials=validated_creds)
        return service
