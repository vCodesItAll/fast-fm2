from app.utils.imports import Base, Column, Integer, String, relationship

class ArtistModel(Base):
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
