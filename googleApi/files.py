from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
class DriveFiles:
    def __init__(self, service = None):
        self.__service=service
        self.__folders_mime="mimeType = 'application/vnd.google-apps.folder'"
        self.__root_folder_id=None

    def get_resource_metadata(self, name):
        '''
        Description: find specific resource in google drive,  by name ( file and folder)
        params: resource name
        return: dict with kind, name, parents field
        '''
        serch_filter = "name="+ "'" + name + "'"
        files_service = self.__service.files()
        list_service  = files_service.list(q = serch_filter,
                                           pageSize=1, 
                                           # all possible fields here:
                                           #https://developers.google.com/drive/api/v3/reference/files
                                           fields="nextPageToken, files(kind, id, name, parents)")
        search_list =list_service.execute()
        if len(search_list['files']) == 0:
            return None
        else:

            return dict(search_list['files'][0])


    def download_file(self, file_id):
        request = self.__service.files().get_media(fileId=file_id)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print (f"Download {int(status.progress() * 100)}.")


    def create_folder(self, folder_name):

        if self.__service:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            files_service = self.__service.files()
            create_service =  files_service.create(body=folder_metadata,fields='id')
            folder_id = create_service.execute()
            return folder_id
        else:
            return "error: no service provided"
