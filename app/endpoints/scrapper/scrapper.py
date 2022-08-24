from fastapi import APIRouter, status
from schemas import URLSchema
from .service import Scrapper

# APIRouter creates path operations for shortener module
router = APIRouter(
    tags=["Scraper App"],
)


@router.post("/url", status_code=status.HTTP_201_CREATED)
def fetch_products_from_url(payload: URLSchema):
    url = payload.url
    scrapper = Scrapper(url)
    result = scrapper.run_scrapper()

    return result
