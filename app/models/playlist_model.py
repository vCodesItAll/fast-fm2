from app.utils.imports import Base, Column, Integer, String, ForeignKey, relationship


class PlaylistModel(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Reference to the users table
    user_id = Column(Integer, ForeignKey('users.id'))  
    # Relationship with users
    user = relationship("User", back_populates="playlists")  
    # Relationship with songs via playlist_songs
    songs = relationship("Song", secondary="playlist_songs", back_populates="playlists")  

    # Implement additional functionality, like returning playlist data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
