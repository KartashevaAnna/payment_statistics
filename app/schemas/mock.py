from typing import List

from pydantic import BaseModel

from app.schemas.company import CompanyUpdateSchema


class Mock(BaseModel):
    companies: List[CompanyUpdateSchema]