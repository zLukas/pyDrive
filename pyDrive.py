from googleApi import api_login
from googleApi import DriveFiles

api_service = api_login()
drive_files = DriveFiles(api_service)
files = drive_files.list_files(10)

for file in files:
    print(file)