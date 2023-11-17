from app.utils.imports import router, get_db, Session, Depends, SessionLocal, APIRouter, controllers, User, UserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return controllers.create_user(db=db, user=user)