from fastapi import APIRouter

from schemas import URLSchema
from .service import Scrapper

# APIRouter creates path operations for shortener module
router = APIRouter(
    tags=["Scraper App"],
)


@router.post("/url")
def fetch_products_from_url(payload: URLSchema):
    url = payload.url
    scrapper = Scrapper(url)
    result = scrapper.run_scrapper()

    return result
