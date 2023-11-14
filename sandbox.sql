/* Create tables for a music library */

Table songs {
  id int [pk, increment]
  title varchar
  duration_seconds int
  release_date date
  // Other song attributes here
}

Table artists {
  id int [pk, increment]
  name varchar
  genre varchar
  // Other artist attributes here
}

Table albums {
  id int [pk, increment]
  title varchar
  release_date date
  // Other album attributes here
}

Table song_artists { // Junction table for many-to-many relationship between songs and artists
  song_id int [ref: > songs.id]
  artist_id int [ref: > artists.id]
  // Other fields related to song-artist relationship
}

Table playlists {
  id int [pk, increment]
  name varchar
  // Other playlist attributes here
}

Table playlist_songs { // Junction table for many-to-many relationship between playlists and songs
  playlist_id int [ref: > playlists.id]
  song_id int [ref: > songs.id]
  // Other fields related to playlist-song relationship
}


Table users {
  id int [pk, increment]
  username varchar
  email varchar
  // Other user attributes here
}

/* Define relationships between tables */

Alter table song_artists drop constraint song_artists_song_id_fkey;
Ref: song_artists.song_id > songs.id
Ref: song_artists.artist_id > artists.id
Ref: playlist_songs.song_id > songs.id
Ref: playlist_songs.playlist_id > playlists.id
// Add more relationships as needed
