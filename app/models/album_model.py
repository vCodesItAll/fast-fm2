from app.utils.imports import Base, Column, Integer, String, Date, ForeignKey, Table, relationship

# # Junction table for many-to-many relationship between albums and artists
# album_artists = Table(
#     'album_artists',
#     Base.metadata,
#     Column('album_id', Integer, ForeignKey('albums.id')),
#     Column('artist_id', Integer, ForeignKey('artists.id'))
# )

class AlbumModel(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_date = Column(Date)
    # Other album attributes here

    # Define many-to-many relationship between albums and artists
    songs = relationship("Song", back_populates="album")
    artists = relationship("Artist", secondary="song_artists", back_populates="albums")

    # Stretch goal - returning album data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
