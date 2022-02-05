class DriveFiles:
    def __init__(self, service) -> None:
        self.__service=service

    def list_files(self, page_size):
        # Call the Drive v3 API
        results = self.__service.files().list(
            pageSize=page_size, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return items
        else:
           return items
    
    def add_files(self, files):
        pass

    def get_files(self, file_name):
        pass