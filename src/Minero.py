#!/usr/bin/python
# -*- coding: utf-8 -*-

import eyed3

song = eyed3.load("Green Day - Jaded.mp3")
print (song.tag.artist)
print (song.tag.album)
print (song.tag.album_artist)
print (song.tag.title)
print (song.tag.track_num)
print (song.tag.disc_num)
print (song.tag.genre)
print (song.tag.release_date)
