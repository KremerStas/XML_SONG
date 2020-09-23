from models import Song
import random
import xml.etree.ElementTree as ET
from defusedxml import minidom

avtor = input().split(', ')  # Формат записи (Название группы-3, название группы-2)
pesni = []

root = ET.Element('CATALOG')

for zapros in avtor:
    elem = ET.SubElement(root, 'CD')
    command = zapros.split('-')
    for art in Song.select().where(Song.artist == command[0]):
        pesni.append(art.song)
    if pesni:
        elem_artist = ET.SubElement(elem, 'ARTIST')
        elem_artist.text = str(command[0])
        for i in range(int(command[1])):
            elem_title = ET.SubElement(elem, 'TITLE')
            title = str(random.choice(pesni))
            elem_title.text = title
    else:
        print('Исполнитель не найден')
    pesni.clear()

tree = ET.ElementTree(root)
put = r'C:\Users\Пользователь\Desktop\example.xml'
tree.write(put)
xml = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
f = open(put, 'w', encoding='utf-8')
f.write(xml)
