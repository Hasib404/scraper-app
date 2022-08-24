from fastapi import APIRouter
from endpoints import scrapper

router = APIRouter()
router.include_router(scrapper.router)
