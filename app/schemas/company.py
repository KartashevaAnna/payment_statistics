import uuid

from pydantic import BaseModel, Field, ValidationError, constr, validator
from pydantic.networks import AnyUrl, EmailStr

from app.enums import CompanyStatus


class OKVED(BaseModel):
    code: constr(min_length=2, max_length=4)
    description: str


class CompanySchema(BaseModel):
    id: uuid.UUID
    org_type: constr(min_length=2, max_length=3) | None
    name: str | None
    inn: constr(min_length=9, max_length=15) | None
    current_account: constr(min_length=9, max_length=20) | None
    activity: OKVED | None
    logo_url: AnyUrl | None
    email: EmailStr | None
    phone_number: str | None
    status: CompanyStatus = Field(default=CompanyStatus.pending_approval)
    is_sanctioned: bool | None
    site_url: AnyUrl | None

    @validator("phone_number")
    def prettify_phone_number(cls, v):
        if not v:
            return None
        v = (v.translate({ord(i): None for i in '+ ()-'}))
        if not v.isdigit():
            raise ValidationError('Phone number must not contain letters')
        return v
