#aplikacja na bazie filmu https://www.youtube.com/watch?v=qbW6FRbaSl0
# kanał Kalle Hallden # 525 tys. subskrybentów
# https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ

#Aplikacja 3 z filmu ma pobrać informację z api do json file i wyświetlić najnowszy film kiedy się ukaże i dopiero wtedy działając w tle
#Błąd przy odczycie/zapisie do pliku json - nie pokazał ponowanie wszystkiego
#Alternatywa - gdy spadnie o 10% akcje otwórz okno
import json
import urllib.request
from selenium import webdriver
import time

def look_for_new_video():


    api_key = "AIzaSyAg4BESmz26dV_0HU4WvAR1x7-FzclZlnU"
    channel_id = "UCWr0mx597DnSGLFk1WfvSkQ" # channel id to nie nazwa kanału - nie wyszstkie mają właczony kanał ID

    #AIzaSyAg4BESmz26dV_0HU4WvAR1x7 - FzclZlnU
    base_video_url = 'https://wwww.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    inp = urllib.request.urlopen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoid.json', 'r', encoding='utf-8', errors='ignore') as json_file:
        data = json.load(json_file, strict=False)
        json_file.close()
        if data['videoId'] != vidID:
            driver = webdriver.Chrome
            driver.get(base_video_url + vidID)
            video_exists = True

    if video_exists:
        with open['videoid.json', 'w'] as json_file:
            data = {'videoId': vidID}
            json.dump(data, json_file)


try:
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stopping')


