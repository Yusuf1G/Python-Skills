import sqlite3

conn = sqlite3.connect('sql3-musicdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    artist_id  INTEGER PRIMARY KEY,
    artist_name    TEXT UNIQUE
);

CREATE TABLE Genre (
    genre_id  INTEGER PRIMARY KEY,
    genre_name    TEXT UNIQUE
);

CREATE TABLE Album (
    album_id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    album_name   TEXT UNIQUE
);

CREATE TABLE Track (
    track_id  INTEGER PRIMARY KEY,
    track_name TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    track_len INTEGER, 
    track_rating INTEGER, 
    track_count INTEGER
);
''')

handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle:
    line = line.strip();
    pieces = line.split(',')
    if len(pieces) < 6 : continue

    track_name = pieces[0]
    artist_name = pieces[1]
    album_name = pieces[2]
    track_count = pieces[3]
    track_rating = pieces[4]
    track_len = pieces[5]
    genre_name = pieces[6]

    print(track_name, artist_name, album_name, track_count, track_rating, track_len, genre_name)

    cur.execute('''INSERT OR IGNORE INTO Artist (artist_name) 
        VALUES ( ? )''', ( artist_name, ) )
    cur.execute('SELECT artist_id FROM Artist WHERE artist_name = ? ', (artist_name, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (album_name, artist_id) 
        VALUES ( ?, ? )''', (album_name, artist_id ) )
    cur.execute('SELECT album_id FROM Album WHERE album_name = ? ', (album_name, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (genre_name) 
        VALUES ( ? )''', (genre_name, ) )
    cur.execute('SELECT genre_id FROM Genre WHERE genre_name = ? ', (genre_name, ))
    genre_id = cur.fetchone()[0]  

    cur.execute('''INSERT OR IGNORE INTO Track (track_name, album_id, genre_id, track_len, track_rating, track_count)
        VALUES ( ?, ?, ? ,?, ?,? )''', (track_name, album_id, genre_id, track_len, track_rating, track_count)), 
    cur.execute('SELECT track_id FROM Track WHERE track_name = ? AND track_len = ? AND track_rating = ? AND track_count = ? ', (track_name, track_len, track_rating, track_count ))
    

    conn.commit()
