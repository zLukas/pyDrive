from googleApi import api_login
from googleApi import DriveFiles
from sys import argv
from configparser import ConfigParser

api_service = api_login()
drive =DriveFiles(api_service)

param = argv[1]

if param == "setup":
    api = drive.get_resource_metadata("api.ini")
    drive.download_file(api['id'])
    data =["parent_dir_id", api['parents'][0]]
    #config = ConfigParser()
    #config.read("api.ini")
    #config["meta"]["parent_dir_id"] = str(api['parents'][0])
    #config.write(config)
