import uuid

from fastapi import APIRouter

from app.schemas.company import CompanySchema
from utils.helpers import get_fake_company

company_router = APIRouter(tags=["Healthcheck"])


@company_router.get("/company/{company_id}")
def get_company(company_id: uuid.UUID) -> CompanySchema:
    """Returns one post."""

    return get_fake_company()
