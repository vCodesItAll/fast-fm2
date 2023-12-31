from app.utils.imports import Base, Column, Integer, ForeignKey, relationship, DateTime


class PlaysModel(Base):
    __tablename__ = "plays"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey('songs.id'))  # Reference to the songs table
    user_id = Column(Integer, ForeignKey('users.id'))  # Reference to the users table
    played_at = Column(DateTime)  # Timestamp when the song was played

    song = relationship("Song", back_populates="plays")  # Relationship with songs
    user = relationship("User", back_populates="plays")  # Relationship with users

    # Implement additional functionality, like returning play data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}