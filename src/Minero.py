#!/usr/bin/python
# -*- coding: utf-8 -*-

import eyed3
import os

song = eyed3.load("Green Day - Jaded.mp3")
print (song.tag.artist)
print (song.tag.album)
print (song.tag.album_artist)
print (song.tag.title)
print (song.tag.track_num)
print (song.tag.disc_num)
print (song.tag.genre)
print (song.tag.release_date)

#regresa la direccion exacta de la carpeta Music
newpath = os.path.expanduser('~/Music')
print (newpath)

#regresa el arbol de direcciones entero (directorios, documentos)
for dirpath, dirnames, filenames in os.walk(newpath):
     print([os.path.join(root,file)])
