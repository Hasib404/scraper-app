from datetime import datetime
from urllib.request import Request
from fastapi import APIRouter, Request, status
from schemas import URLSchema
from database import User

# APIRouter creates path operations for shortener module
router = APIRouter(
    tags=["Scraper App"],
    responses={404: {"description": "Not found"}},
)


@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(payload: URLSchema):
    payload.email = payload.email.lower()
    User.insert_one(dict(payload))
    return {
        "status": "success",
    }
