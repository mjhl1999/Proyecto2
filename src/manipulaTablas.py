#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

#Connect with database
conn = sqlite3.connect("songs.db")

#Query cursor
c = conn.cursor()


def performers_entry(id_performer, id_type, name):
    c.execute('''INSERT INTO performers VALUES(
                id_performer,
                id_type,
                name)''')

def personas_entry(id_person, stage_name, real_name, birth_date, death_date):
    c.execute('''INSERT INTO persons VALUES(
                 id_person,
                 stage_name,
                 Real_name,
                 birth_date,
                 death_date)''')

def groups_entry(id_group, name, start_date, end_date):
    c.execute('''INSERT INTO groups VALUES(
                 id_group,
                 name,
                 start_date,
                 end_date)''')

def albums_entry(id_album, path, name, year):
    c.execute('''INSERT INTO albums VALUES(
                 id_album,
                 path,
                 name,
                 year)''')

def rolas_entry(id_rola, id_performer, id_album, path, title, track, year, genre):
    c.execute('''INSERT INTO rolas VALUES(
                 id_rola,
                 performer,
                 id_album,
                 path,
                 title,
                 track,
                 year,
                 genre)''')

def group_entry(id_person, id_group):
    c.execute('''INSERT INTO TABLE in_group VALUES(
                 id_person,
                 id_group)''')
