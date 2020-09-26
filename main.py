from models import Song
import random
import xml.etree.ElementTree as ET
from defusedxml import minidom
import os

author = input().split(', ')  # Формат записи (Название группы-3, название группы-2)
songs = []

root = ET.Element('CATALOG')

for requests in author:
    elem = ET.SubElement(root, 'CD')
    command = requests.split('-')
    for art in Song.select().where(Song.artist == command[0]):
        songs.append(art.song)
    if songs:
        elem_artist = ET.SubElement(elem, 'ARTIST')
        elem_artist.text = str(command[0])
        for i in range(int(command[1])):
            elem_title = ET.SubElement(elem, 'TITLE')
            title = str(random.choice(songs))
            elem_title.text = title
    else:
        print('Исполнитель не найден')
    songs.clear()

tree = ET.ElementTree(root)
path = os.getcwd()
path_xml = os.path.join(path, 'example.xml')
tree.write(path_xml)
xml = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
f = open(path_xml, 'w', encoding='utf-8')
f.write(xml)
