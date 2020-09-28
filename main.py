from models import Song
import random
import xml.etree.ElementTree as ET
from defusedxml import minidom
import os


class XmlSongs:
    def __init__(self, request):
        self.root = ET.Element('CATALOG')
        self.request = {}
        requests = request.split(', ')
        for artist in requests:
            self.request[artist[0: artist.rindex(' ')]] = int(artist[artist.rindex(' ') + 1::])

    @staticmethod
    def check_artist(artist):
        songs = []
        for art in Song.select().where(Song.artist == artist):
            if art.song not in songs:
                songs.append(art.song)
        if songs:
            return songs
        else:
            raise ValueError('Исполнитель {} не найден'.format(artist))

    def _build_xml(self):
        for artist in self.request.keys():
            try:
                songs = XmlSongs.check_artist(artist)
                if songs:
                    elem = ET.SubElement(self.root, 'CD')
                    elem_artist = ET.SubElement(elem, 'ARTIST')
                    elem_artist.text = str(artist)
                    self._elem_title(elem, artist, songs)
            except ValueError as err:
                print(err)

    def _elem_title(self, elem, artist, songs):
        if len(songs) < self.request[artist]:
            counter = len(songs)
            print('Вы запросили {count} треков, а всего у артиста {all} песен'.format(count=self.request[artist],
                                                                                      all=len(songs)))
        else:
            counter = self.request[artist]
        for index in range(counter):
            elem_title = ET.SubElement(elem, 'TITLE')
            elem_title.text = str(random.choice(songs))

    def create_xml(self):
        self._build_xml()
        tree = ET.ElementTree(self.root)
        path_xml = os.path.join(os.getcwd(), 'example.xml')
        tree.write(path_xml)
        xml = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
        f = open(path_xml, 'w', encoding='utf-8')
        f.write(xml)
        f.close()


result = XmlSongs(input())
result.create_xml()
