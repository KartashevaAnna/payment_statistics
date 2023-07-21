import uuid

from fastapi import APIRouter, Request, Body, HTTPException

from app.enums import CompanyStatus
from app.models.company import Company
from app.schemas.company import CompanyUpdateSchema, CompanyCreateSchema, CompanyFakeSchema
from utils.helpers import get_fake_company

company_router = APIRouter(tags=["Company"])
company_fake_router = APIRouter(tags=["Fake Company"])

company_list = []


@company_fake_router.post("/company/fake", summary='Create a fake company')
def get_company() -> CompanyFakeSchema:
    return get_fake_company()


@company_router.post("/company", summary='Create a company', status_code=201)
async def create_company(body: CompanyCreateSchema = Body(), ) -> str:
    await Company(**body.dict()).save()
    return "Company has been successfully created."


@company_router.get("/companies", summary="Show all companies")
async def get_company(request: Request):
    return await Company.all()


@company_router.get("/company/{company_id}", summary='Show one company')
async def get_company(company_id: uuid.UUID):
    return await Company.get_or_none(id=company_id)


@company_router.post("/update/{company_id}", summary='Update company', status_code=200)
async def update_company(company_id: uuid.UUID, body: CompanyUpdateSchema) -> str:
    old_company = await Company.get_or_none(id=company_id)
    if not old_company:
        raise HTTPException(status_code=404, detail=f'Company with id {company_id} not found')
    new_data = body.dict(exclude_none=True)
    await old_company.update_from_dict(new_data)
    await old_company.save()
    return f'Company with id {company_id} successfully updated.'


@company_router.delete("/delete/{company_id}", summary='Delete  company', status_code=200)
async def delete_company(company_id: uuid.UUID) -> str:
    company = await Company.get_or_none(id=company_id)
    await company.delete()
    await company.save()
    return f'Company with id {company_id} successfully deleted.'


@company_router.post("/company/{company_id}/edit-status", summary='Edit company status', status_code=200)
async def update_company_status(company_id: uuid.UUID, body: CompanyStatus = Body(), ) -> str:
    company = await Company.get_or_none(id=company_id)
    company.status = body
    await company.save()
    return f'Company status with id {company_id} is set to {body.name}.'
