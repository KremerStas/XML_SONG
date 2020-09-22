from peewee import *

db = SqliteDatabase('song.db')


class Song(Model):
    artist = CharField()
    song = CharField()

    class Meta:
        database = db

