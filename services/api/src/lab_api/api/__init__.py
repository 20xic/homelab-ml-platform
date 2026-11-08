from fastapi import APIRouter

from lab_api.core import settings

from .endpoints import router as endpoints_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(endpoints_router)
