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
drive =DriveFiles(api_service)

param = argv[1]

def check_download_folder():
    if  not path.exists(DOWNLOAD_DIR):
        mkdir(DOWNLOAD_DIR)
    else:
        pass


if param == "setup":
    check_download_folder()

    drive_dir = argv[2]
    if drive_dir == None:
        print("no directory provided")
    else:
        # validate directory
        directory_meta = drive.get_resource_metadata(drive_dir)
        if drive_dir is not None:
            environ["PYDRIVE_UPLOAD_FOLDER"] = drive_dir
            print("target directory set")
        else:
            print("no such directory in drive")

    
elif param == "pull":
    check_download_folder()
    resource_name = argv[2]
    file_meta = drive.get_resource_metadata(resource_name)
    if file_meta is not None:
        base_dir = getcwd()
        chdir(DOWNLOAD_DIR)
        drive.download_file(file_meta['id'], file_meta['name'])
        chdir(base_dir)
    else:
        print("file not exist")    
    



elif param == "push":
    pass

