from pydantic import BaseModel
from typing import List

from app.schemas.company import CompanySchema


class Mock(BaseModel):
    companies: List[CompanySchema]