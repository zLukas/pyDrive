from googleApi import DriveFiles
from googleApi import DriveLogin
from sys import argv
from os import environ
from os import mkdir
from os import path
from os import chdir
from os import getcwd


DOWNLOAD_DIR='downloads'
login = DriveLogin()
api_service = login.api_login()
drive = DriveFiles(api_service)

param = argv[1]
  
if param == "pull":
    if  not path.exists(DOWNLOAD_DIR):
        mkdir(DOWNLOAD_DIR)
    else:
        pass

    resource_name = argv[2]
    base_dir = getcwd()
    chdir(DOWNLOAD_DIR)
    drive.download_file(resource_name)
    chdir(base_dir)   
    
elif param == "push":
    if len(argv) < 4:
        print("file or dir empty")
    else:
        file = argv[2]
        dir = argv[3]
        folder_meta = drive.get_resource_metadata(dir)
        upload_id = drive.upload_file('test.txt', folder_meta['id'])
        print(f" uploaded file id: {upload_id} ")
