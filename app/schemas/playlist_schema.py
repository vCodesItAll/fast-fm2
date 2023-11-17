from app.utils.imports import BaseModel


class PlaylistBase(BaseModel):
    name: str
    user_id: int

class PlaylistCreate(PlaylistBase):
    pass

class Playlist(PlaylistBase):
    id: int

    class Config:
        orm_mode = True
