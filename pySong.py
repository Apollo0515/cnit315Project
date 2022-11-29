import asyncio
import sys
import requests
import vlc
import time




def YoutubeLookup():
    global youtubeID
    name = str(sys.argv[1])
    url = "https://youtube-v2.p.rapidapi.com/search/"

    querystring = {"query": name, "lang": "en", "country": "us"}

    headers = {
        "X-RapidAPI-Key": "f0e0bb49b8msh380d03d27aa5fc7p19f33ajsna47ae205484d",
        "X-RapidAPI-Host": "youtube-v2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json = str(response.text)
    splitting = json.split('"')
    youtubeID = splitting[87]
    #print(response.text)


def YoutubeConvert():
    global Mp3URL
    array = []
    youtubeURL = "https://www.youtube.com/watch?v=" + youtubeID
    url = "https://t-one-youtube-converter.p.rapidapi.com/api/v1/createProcess"
    querystring = {"url": youtubeURL, "format": "mp3", "responseFormat": "json", "stop": "30", "lang": "en"}
    headers = {
        "X-RapidAPI-Key": "f0e0bb49b8msh380d03d27aa5fc7p19f33ajsna47ae205484d",
        "X-RapidAPI-Host": "t-one-youtube-converter.p.rapidapi.com"
    }
    while(True):
        response = requests.request("GET", url, headers=headers, params=querystring)
        json = str(response.text)
        split = json.split('"')
        print(response.text)
        try:
            theURL = split[11]
            ugh = theURL.split('\\')
            s = ""
            for i in ugh:
                array.append(i)
                Mp3URL = s.join(array)
            print(Mp3URL)
            #print(response.text)
            break
        except:
            time.sleep(2)

def play():
    p = vlc.MediaPlayer(Mp3URL)
    p.play()
    time.sleep(30)

def doSomething():
    print('Hi')

def main():
    YoutubeLookup()
    YoutubeConvert()
    play()

main()