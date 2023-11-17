from app.utils.imports import Base, Column, Integer, String, Date, ForeignKey, Table, relationship


class GenreModel(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Other genre attributes here

    # Relationship with songs via song_genres
    songs = relationship("Song", secondary="song_genres", back_populates="genres") 

    # Return genre data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}