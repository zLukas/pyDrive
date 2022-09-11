from .files import DriveFiles
from .login import DriveLogin
from os import mkdir
from os import path
from os import chdir
from os import getcwd


class Drive(DriveLogin, DriveFiles):
    def __init__(self, creds_path) -> None:
        super().__init__(creds_path)
        self.__service = self.api_login()
    
    def download_file(drive_object,file_name, download_dir):
        if  not path.exists(download_dir):
            mkdir(download_dir)
        base_dir = getcwd()
        chdir(download_dir)
        drive_object.download_file(file_name)
        chdir(base_dir) 

    def upload_file(self,file_name, upload_dir):
        folder_meta = self.get_resource_metadata(upload_dir)
        file_id = self.upload_file(file_name, folder_meta['id'])
        return file_id
        