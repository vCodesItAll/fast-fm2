from app.utils.imports import router, APIRouter, creates


router = APIRouter()

router.include_router(creates.router)


