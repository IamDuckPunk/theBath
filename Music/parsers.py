from bs4 import BeautifulSoup
import re
import unicodedata
from urllib import request
from datetime import datetime
from django.shortcuts import render, get_object_or_404



def slugify(string):
    return (((string.strip()).replace(' ', '_')).title())


def get_html(string):
    url = 'https://en.wikipedia.org/wiki/'
    url = url + slugify(string)
    response = request.urlopen(url)
    return response.read()


def parse(string):
    info = []
    soup = BeautifulSoup(get_html(string), "html.parser")
    table = soup.find('table', class_='infobox vevent haudio')
    songs_list = soup.find('table', class_='tracklist')
    songs = songs_list.find_all('tr')

    headers_list = list(filter(None, songs[0].get_text().split('\n'))) # List of headers 
    #headers = {item: item for item in headers_list}
    songs_list = []

    for song in songs[1:]:
        song = song.get_text().split('\n')[1:-1]
        songs_list.append(song)

    for row in filter(None, table.get_text().split('\n')):
        info.append(row)

    album_info = {
        'Released': info[(info.index('Released')) + 1],
        'Studio': info[(info.index('Studio')) + 1],
        'Genre': info[(info.index('Genre')) + 1],
        'Producer': info[(info.index('Producer')) + 1]
    }
    return album_info, headers_list, songs_list





