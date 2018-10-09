#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

#Connect with database
conn = sqlite3.connect("songs.db")

#Query cursor
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS types(
             id_type      INTEGER PRIMARY KEY,
             description   TEXT);''')

c.execute('''INSERT INTO types VALUES (0,'Person')''')
c.execute('''INSERT INTO types VALUES (1,'Group')''')
c.execute('''INSERT INTO types VALUES (2,'Unknown')''')

c.execute('''CREATE TABLE performers(
            id_performer   INTEGER PRIMARY KEY,
            id_type        INTEGER,
            name           TEXT,
            FOREIGN KEY (id_type) REFERENCES types(id_type))''')


c.execute('''CREATE TABLE persons(
            id_person      INTEGER PRIMARY KEY,
            stage_name      TEXT,
            real_name       TEXT,
            birth_date      TEXT,
            death_date      TEXT)''')

c.execute('''CREATE TABLE groups(
             id_group      INTEGER PRIMARY KEY,
             name          TEXT,
             start_date    TEXT,
             end_date      TEXT)''')

c.execute('''CREATE TABLE albums(
             id_album      INTEGER PRIMARY KEY,
             path          TEXT,
             name          TEXT,
             year          INTEGER)''')

c.execute('''CREATE TABLE rolas(
             id_rola       INTEGER PRIMARY KEY,
             id_performer  INTEGER,
             id_album      INTEGER,
             path          TEXT,
             title         TEXT,
             track         INTEGER,
             year          INTEGER,
             genre         TEXT,
             FOREIGN KEY   (id_performer) REFERENCES performers(id_performer),
             FOREIGN KEY   (id_album) REFERENCES albums(id_album))''')

c.execute('''CREATE TABLE in_group(
             id_person     INTEGER,
             id_group      INTEGER,
             PRIMARY KEY   (id_person, id_group),
             FOREIGN KEY   (id_person) REFERENCES persons(id_person),
             FOREIGN KEY   (id_group) REFERENCES  groups(id_group))''')

conn.commit()
conn.close()
