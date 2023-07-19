import uuid
from typing import List

from fastapi import APIRouter, Request, Body, Response

from app.enums import CompanyStatus
from app.schemas.company import CompanySchema
from utils.helpers import get_fake_company

company_router = APIRouter(tags=["Company"])

company_list = []


@company_router.post("/company/fake", summary='Create a fake company', tags=['Fake Company'])
def get_company() -> CompanySchema:
    return get_fake_company()


@company_router.post("/company", summary='Create a company')
def get_company(body: CompanySchema = Body(), ) -> Response:
    print(body)
    return 'OK'


@company_router.get("/companies", summary="Show all companies")
def get_company(request: Request) -> List[CompanySchema]:
    return request.app.state.mock.companies


@company_router.get("/company/{company_id}", summary='Show one company')
def get_company(company_id: uuid.UUID) -> CompanySchema:
    return get_fake_company()


@company_router.post("/update/{company_id}", summary='Update company', status_code=200)
def update_company(company_id: uuid.UUID, body: CompanySchema = Body(), ) -> str:
    return f'Company with id {company_id} successfully updated.'


@company_router.delete("/delete/{company_id}", summary='Delete  company', status_code=200)
def delete_company(company_id: uuid.UUID) -> str:
    return f'Company with id {company_id} successfully deleted.'


@company_router.post("/company/{company_id}/edit-status", summary='Edit company status', status_code=200)
def delete_company(company_id: uuid.UUID, body: CompanyStatus = Body(),) -> str:
    return f'Company status with id {company_id} is set to {body.name}.'
