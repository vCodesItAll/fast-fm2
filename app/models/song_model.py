from app.utils.imports import Base, Column, Integer, String, Date, ForeignKey, relationship


class SongModel(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    duration_seconds = Column(Integer)
    release_date = Column(Date)
    album_id = Column(Integer, ForeignKey('albums.id'))  # Reference to the albums table

    album = relationship("Album", back_populates="songs")  # Relationship with albums
    artists = relationship("Artist", secondary="song_artists", back_populates="songs")  # Relationship with artists via song_artists
    playlists = relationship("Playlist", secondary="playlist_songs", back_populates="songs")  # Relationship with playlists via playlist_songs
    genres = relationship("Genre", secondary="song_genres", back_populates="songs")  # Relationship with genres via song_genres
    plays = relationship("Play", back_populates="song")  # Relationship with plays

    # Implement additional functionality, like returning song data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
