#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class DAO(object):

    #Connect with database
    conn = sqlite3.connect("songs.db")

    #Query cursor
    c = conn.cursor()


    def terminar(self):
        self.conn.commit()
        self.conn.close()

    def performers_entry(self, id_type, name):
        self.c.execute('''INSERT INTO performers(id_type, name) VALUES(?,?)''',(id_type, name,))
        self.terminar()

    def persons_entry(self, stage_name):
        self.c.execute('''INSERT INTO persons(stage_name) VALUES(?)''',(stage_name,))
        self.terminar()

    def groups_entry(self, name):
        self.c.execute('''INSERT INTO groups(name) VALUES(?)''',(name,))
        self.terminar()

    def albums_entry(self, path, name, year):
        self.c.execute('''INSERT INTO albums(path, name, year) VALUES(?,?,?)''',(path, name, year,))
        self.terminar()

    def rolas_entry(self, id_performer, id_album, path, title, track, year, genre):
        self.c.execute('''INSERT INTO rolas(id_performer, id_album, path, title, track, year, genre)
                          VALUES(?,?,?,?,?,?,?)''',(id_performer, id_album, path, title, track, year, genre,))
        self.terminar()


objeto = DAO()
