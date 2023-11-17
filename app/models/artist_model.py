from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime# # Pivot table for many-to-many relationship between albums and artists
# album_artists = Table(
#     'album_artists',
#     Base.metadata,
#     Column('album_id', Integer, ForeignKey('albums.id')),
#     Column('artist_id', Integer, ForeignKey('artists.id'))
# )

# # Pivot table for many-to-many relationship between songs and artists
# song_artists = Table(
#     'song_artists',
#     Base.metadata,
#     Column('song_id', Integer, ForeignKey('songs.id')),
#     Column('artist_id', Integer, ForeignKey('artists.id'))
# )

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = Column(String)
    # Other artist attributes here

    # Relationship with albums via song_artists
    albums = relationship("Album", secondary="song_artists", back_populates="artists")

    # Relationship with songs via song_artists
    songs = relationship("Song", secondary="song_artists", back_populates="artists")

    # Stretch goal returning artist data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
