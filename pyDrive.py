from googleApi import Drive
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


def main():
    params = get_input()
    drive = Drive()
    login = DriveLogin(params.credentials)
    drive = DriveFiles(login.api_login())
    if params.upload not None:
        download_file(drive, param.files, param.destination)
    else:
        upload_file(drive, param.files, param.destination)
    

if __name__ == '__main__':
    main()
