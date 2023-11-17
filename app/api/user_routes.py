from app.utils.imports import router, APIRouter
from app.utils import creates

router = APIRouter()

router.include_router(creates.router)


