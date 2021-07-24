#-------------------------------#
# App Name: Lofi - Audio Player |
# Description: -                |
# Author : jay-sb               |
# Date : 21-07-2021             |
#-------------------------------#

import requests
from requests_html import HTMLSession
import json
import os
import googleapiclient.discovery
import webbrowser
import random

url = 'https://www.youtube.com/watch?v='
theme = input('ambiance?\n')
theme = theme.replace(' ', '+')
chpath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "YOUR_DEVELOPER_KEY"

youtube = googleapiclient.discovery.build(
api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.search().list(
    part="snippet",
    q="lofi"+'+{}'.format(theme)
)

reponse = request.execute()
url_list = []

for items in reponse['items']:
    for video in items['id'].items():
        if video[0]=='videoId':
            print(video[1]) 
            url_list.append(video[1])

number = random.randint(0,4)

url=url+'{}'.format(url_list[number])
webbrowser.get(chpath).open(url)
