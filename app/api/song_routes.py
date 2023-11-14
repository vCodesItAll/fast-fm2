from fastapi import APIRouter

router = APIRouter()

# Get all songs
@router.get("/api/v1/songs")
async def get_songs():
    # Logic to fetch all songs
    return {"message": "List of all songs"}

# Get a single song by ID
@router.get("/api/v1/songs/{song_id}")
async def get_song(song_id: int):
    # Logic to fetch a song by ID
    return {"message": f"Details of song with ID {song_id}"}

# Create a new song
@router.post("/api/v1/songs")
async def create_song():
    # Logic to create a new song
    return {"message": "Create a new song"}

# Update a song by ID
@router.put("/api/v1/songs/{song_id}")
async def update_song(song_id: int):
    # Logic to update a song by ID
    return {"message": f"Update song with ID {song_id}"}

# Delete a song by ID
@router.delete("/api/v1/songs/{song_id}")
async def delete_song(song_id: int):
    # Logic to delete a song by ID
    return {"message": f"Delete song with ID {song_id}"}
