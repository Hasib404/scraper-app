from fastapi import APIRouter
from endpoints.scrapper import scrapper

router = APIRouter()
router.include_router(scrapper.router)
