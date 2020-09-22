import requests
from bs4 import BeautifulSoup
from models import Song


for index_artist in range(11, 99):
    pars = requests.get('https://music.yandex.ru/artist/410{}/tracks'.format(index_artist))
    soup = BeautifulSoup(pars.text, 'html.parser')
    for song in soup.find_all('div', class_='d-track__quasistatic-column'):
        songs = song.string
        artists = soup.find('h1', class_='page-artist__title typo-h1 typo-h1_big').string
        if songs is None:
            continue
        artistes = Song(artist=artists, song=songs)
        artistes.save()

