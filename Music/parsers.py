from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime
from django.shortcuts import render, get_object_or_404
import requests
from PIL import Image
from io import BytesIO
def slugify(string):
    """" Makes a titile slug from the given string """

    return (((string.strip()).replace(' ', '_')).title())


def get_html(string):
    """ Read wiki html page """

    url = 'https://en.wikipedia.org/wiki/'
    url = url + slugify(string)
    response = request.urlopen(url)
    print('Trying to get', url)
    return response.read()


def parse(string):
    """ Parse wiki page for info """

    info = []
    soup = BeautifulSoup(get_html(string), "html.parser")
    table = soup.find('table', class_='infobox vevent haudio')
    songs_list = soup.find('table', class_='tracklist')
    songs = songs_list.find_all('tr')
    headers_list = list(filter(None, songs[0].get_text().split('\n'))) # List of headers 
    headers_list =  headers_list[:2] +  headers_list[-1:]  
    songs_list = []
    for song in songs[1:]:
        song = song.get_text().split('\n')[1:-1]
        songs_list.append(song[:2] + song[-1:])
    for row in filter(None, table.get_text().split('\n')):
        info.append(row)
    album_info = {
        'Released': info[(info.index('Released')) + 1],
        #'Studio': info[(info.index('Studio')) + 1],
        #'Genre': info[(info.index('Genre')) + 1],
        'Producer': info[(info.index('Producer')) + 1]
    }
    return album_info, headers_list, songs_list


def get_image(string):
    """             """
    try:
        plusgify =  (((string.strip()).replace(' ', '+')).lower())
        google_api = "https://www.google.ru/search?q=%s&newwindow=1&hl=ru&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiblNWqoZ3YAhVFP5oKHaYwAYMQ_AUICigB&biw=1375&bih=785#imgrc=XcJ7xLfTaaf5cM:" % (plusgify)
        #url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Mos_Def_-_Ilosaarirock_2012.jpg/1200px-Mos_Def_-_Ilosaarirock_2012.jpg"
        #print(google_api)
        response = requests.get(google_api)
        img = Image.open(BytesIO(response.content))
        img.show()
    except Exception as err:
        print(err)








#album_info, headers_list, songs_list, link_image = parse('No One Ever Really Dies')



