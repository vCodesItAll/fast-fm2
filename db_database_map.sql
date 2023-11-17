-- Table for Songs
CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    duration_seconds INT,
    release_date DATE
);

-- Table for Artists
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    genre VARCHAR
);

-- Table for Albums
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    release_date DATE
);

-- Pivot table for many-to-many relationship between songs and artists
CREATE TABLE song_artists (
    song_id INT REFERENCES songs(id),
    artist_id INT REFERENCES artists(id),
    PRIMARY KEY (song_id, artist_id)
);

-- Bridge table for many-to-many relationship between albums and songs
CREATE TABLE album_songs (
    album_id INT REFERENCES albums(id),
    song_id INT REFERENCES songs(id),
    order INT,
    PRIMARY KEY (album_id, song_id)
);

-- Table for Playlists
CREATE TABLE playlists (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    user_id INT
);

-- Pivot table for many-to-many relationship between playlists and songs
CREATE TABLE playlist_songs (
    id SERIAL PRIMARY KEY,
    playlist_id INT REFERENCES playlists(id),
    song_id INT REFERENCES songs(id),
    order INT
);

-- Table for Users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR,
    email VARCHAR
);

-- Table for Plays
CREATE TABLE plays (
    id SERIAL PRIMARY KEY,
    song_id INT REFERENCES songs(id),
    user_id INT REFERENCES users(id),
    played_at TIMESTAMP
);

-- Table for Genres
CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

-- Table for song_genres relationship
CREATE TABLE song_genres (
    song_id INT REFERENCES songs(id),
    genre_id INT REFERENCES genres(id),
    PRIMARY KEY (song_id, genre_id)
);

-- Table for song_likes
CREATE TABLE song_likes (
    user_id INT REFERENCES users(id),
    song_id INT REFERENCES songs(id),
    PRIMARY KEY (user_id, song_id)
);

-- Table for song_favorites
CREATE TABLE song_favorites (
    user_id INT REFERENCES users(id),
    song_id INT REFERENCES songs(id),
    PRIMARY KEY (user_id, song_id)
);

-- Table for album_likes
CREATE TABLE album_likes (
    user_id INT REFERENCES users(id),
    album_id INT REFERENCES albums(id),
    PRIMARY KEY (user_id, album_id)
);

-- Table for album_favorites
CREATE TABLE album_favorites (
    user_id INT REFERENCES users(id),
    album_id INT REFERENCES albums(id),
    PRIMARY KEY (user_id, album_id)
);

-- Table for song_plays
CREATE TABLE song_plays (
    song_id INT REFERENCES songs(id),
    user_id INT REFERENCES users(id),
    play_count INT,
    PRIMARY KEY (song_id, user_id)
);

-- Table for song_downloads
CREATE TABLE song_downloads (
    song_id INT REFERENCES songs(id),
    user_id INT REFERENCES users(id),
    download_count INT,
    PRIMARY KEY (song_id, user_id)
);


ALTER TABLE "menu_items" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");

ALTER TABLE "menu_items" ADD FOREIGN KEY ("cuisine_id") REFERENCES "cuisines" ("id");
