#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class DAO(object):

    conn = sqlite3.connect("rolas.db")

    c = conn.cursor()

    c.execute('''INSERT INTO groups VALUES(
                 3,
                 'Los rosados',
                 '2028',
                 '1234')''')
