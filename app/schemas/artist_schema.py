from app.utils.imports import BaseModel

class ArtistBase(BaseModel):
    name: str
    genre: str

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int

    class Config:
        orm_mode = True