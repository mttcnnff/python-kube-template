from fastapi import APIRouter

from spend_api.api.root import root_router


router = APIRouter()
router.include_router(root_router, tags=["root"])

