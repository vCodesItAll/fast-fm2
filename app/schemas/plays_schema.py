from app.utils.imports import BaseModel, Optional

class PlaysBase(BaseModel):
    song_id: int
    user_id: int
    played_at: Optional[str]

class PlaysCreate(PlaysBase):
    pass

class Plays(PlaysBase):
    id: int

    class Config:
        orm_mode = True
