import datetime
from pickle import TRUE
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE='client_secret_85604694099-ha1a7utc728g25k11ffl9lv6644jm4kg.apps.googleusercontent.com.json'
API_NAME='youtube'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/youtube.upload']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

Date_Time_of_upload=datetime.datetime(2021,6,26,00,40,0).isoformat() +'.000Z'

request_body={
    'snippet':{
        'categoryId': 23,
        'title': 'test upload',
        'description':':)',
        'tags':['#test','#uploadtest']
    },
    'status':{
        'privacyStatus':'public',
        'publishAt':Date_Time_of_upload,
        'selfDeclareMadeForKids': False
    },
    'notifySubscribers':False
}

mediafile=MediaFileUpload('output.mp4')


response_upload=service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediafile
).execute()





'''
service.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('Erwin Schrodinger.jpg')
).execute()
'''