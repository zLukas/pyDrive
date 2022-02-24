# pyDrive
Python command line tool for simple google drive management, using [Python Google Drive api](https://github.com/googleworkspace/python-samples). 
tool features:
- upload files
- download files

[google API docs](https://developers.google.com/drive/api/v3/about-sdk)

# prequsities
* pipenv
* google account
* GCP cloud project([details](https://cloud.google.com))
* Enabled Drive API ([details](https://developers.google.com/workspace/guides/create-project))
* OAuth2 client ID credential (with .json file)([details](https://developers.google.com/workspace/guides/create-credentials))
* Test users For Google Oauth Api defined In Google Console([details](https://support.google.com/cloud/answer/10311615?hl=en#publishing-status&zippy=%2Cexternal%2Ctesting))

# Usage

Enable pipenv:  
```
cd pyDrive/
$ pipenv shell
$ (pyDrive) pipenv install 
```


Get files from google drive:  
```
$ python3 pyDrive.py pull <file name>
```

upload a file to google drive:  
```
$ python3 pyDrive.py push <Drive folder> <file to upload>
```

at first run google will ask you to grant access for application:
```
$ python3 pyDrive.py pull file.txt
Please visit this URL to authorize this application: <url>

```
follow the link to authorize the application.  
This autorization is a one time event, unless you change/update token.json file
