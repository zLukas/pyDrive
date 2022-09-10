from googleApi import DriveFiles
from googleApi import DriveLogin
from sys import argv
from os import environ
from os import mkdir
from os import path
from os import chdir
from os import getcwd
import argparse


def get_input():

    parser=argparse.ArgumentParser()
    parser.add_argument('--credentials', help='credentials file to send ', required=True)
    parser.add_argument('--upload', help='upload file to drive',action='store_true',  required=False)
    parser.add_argument('--download', help='download file to drive',action='store_true',  required=False)
    parser.add_argument('--files',  help='files names', nargs='+', required=True)
    parser.add_argument('--destination', help='files destination dir ', required=True)

    return parser.parse_args()


def upload_file(drive_object,file_name, upload_dir):
    folder_meta = drive_object.get_resource_metadata(upload_dir)
    upload_id = drive_object.upload_file(file_name, folder_meta['id'])
    print(f" uploaded file id: {upload_id} ")


def download_file(drive_object,file_name, download_dir):
    if  not path.exists(download_dir):
        mkdir(download_dir)
    base_dir = getcwd()
    chdir(download_dir)
    drive_object.download_file(file_name)
    chdir(base_dir) 


def main():
    params = get_input()
    login = DriveLogin(params.credentials)
    drive = DriveFiles(login.api_login())
    if params.upload not None:
        download_file(drive, param.files, param.destination)
    else:
        upload_file(drive, param.files, param.destination)
    





if __name__ == '__main__':
    main()





def run_drive(command,
              local_download_dir,
              remote_dir,
              resource_name
              ):

    login = DriveLogin()
    api_service = login.api_login()
    drive = DriveFiles(api_service)
  
    if command == "pull":
        if  not path.exists(local_download_dir):
            mkdir(local_download_dir)
        else:
            pass

        base_dir = getcwd()
        chdir(local_download_dir)
        drive.download_file(resource_name)
        chdir(base_dir)   
    elif command == "push":
        if len(argv) < 4:
            print("file or dir empty")
        else:

            folder_meta = drive.get_resource_metadata(remote_dir)
            upload_id = drive.upload_file(resource_to_send, folder_meta['id'])
            print(f" uploaded file id: {upload_id} ")

param = argv[1]
resource_name = argv[2]
file = argv[2]
dir = argv[3]



