import uuid

from pydantic import BaseModel, Field, ValidationError, constr, validator
from pydantic.networks import AnyUrl, EmailStr

from app.enums import CompanyStatus


class OKVED(BaseModel):
    code: constr(min_length=2, max_length=4)
    description: str


class CompanyUpdateSchema(BaseModel):
    org_type: constr(min_length=2, max_length=3) | None
    name: str | None
    inn: constr(min_length=9, max_length=15) | None
    current_account: constr(min_length=9, max_length=20) | None
    activity: str | None
    logo_url: AnyUrl | None
    email: EmailStr | None
    phone_number: str | None
    is_sanctioned: bool | None
    site_url: AnyUrl | None

    # @validator("*", pre=True)
    # def empty_str_to_none(cls, v):
    #     if v == "":
    #         return None
    #     return v

    @validator("phone_number")
    def prettify_phone_number(cls, v):
        if not v:
            return None
        res = (v.translate({ord(i): None for i in '+ ()-'}))
        if not res.isdigit():
            raise ValidationError('Phone number must not contain letters')
        return res


class CompanyCreateSchema(CompanyUpdateSchema):
    status: CompanyStatus = Field(default=CompanyStatus.pending_approval)


class CompanyFakeSchema(CompanyCreateSchema):
    id: uuid.UUID
