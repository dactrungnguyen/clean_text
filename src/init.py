import sqlite3

c = sqlite3.connect('db/clean_text.db')
c.execute('DROP TABLE IF EXISTS runs')
c.execute('CREATE TABLE runs (id TEXT, input TEXT, output TEXT)')
c.close()
