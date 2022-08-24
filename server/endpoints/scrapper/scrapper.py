from datetime import datetime
from urllib.request import Request
from fastapi import APIRouter, Request, status
from schemas import URLSchema
from database import URL

# APIRouter creates path operations for shortener module
router = APIRouter(
    tags=["Scraper App"],
    responses={404: {"description": "Not found"}},
)


@router.post("/url", status_code=status.HTTP_201_CREATED)
def generate_page_urls(payload: URLSchema):
    url = payload.url

    URL.insert_one(dict(payload))
    return {
        "status": "success",
    }
