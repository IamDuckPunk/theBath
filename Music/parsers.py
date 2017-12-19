from bs4 import BeautifulSoup
import re
import unicodedata
from urllib import request
from datetime import datetime


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

    for row in filter(None, table.get_text().split('\n')):
        info.append(row)
    album_info = {
        'Released': info[(info.index('Released')) + 1],
        'Studio': info[(info.index('Studio')) + 1],
        'Genre': info[(info.index('Genre')) + 1],
        'Producer': info[(info.index('Producer')) + 1]
    }
    return album_info
string = 'de la soul is dead'
resp = parse(string)
print(resp)

string = 'ok computer'
resp = parse(string)
print(resp)

string = 'Humanz'
resp = parse(string)
print(resp)

string = 'The Fall (Gorillaz album)'
resp = parse(string)
print(resp)
