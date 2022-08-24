from fastapi import APIRouter

from schemas import URLSchema
from .service import Scrapper

# APIRouter creates path operations for Scrapper module
router = APIRouter(
    tags=["Scrapper App"],
)


@router.post("/url")
def fetch_products_from_url(payload: URLSchema):
    url = payload.url
    scrapper = Scrapper(url)
    result = scrapper.run_scrapper()

    return result
