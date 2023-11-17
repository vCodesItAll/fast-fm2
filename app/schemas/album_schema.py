from app.utils.imports import BaseModel, Optional

class AlbumBase(BaseModel):
    title: str
    release_date: Optional[str]

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: int

    class Config:
        orm_mode = True
