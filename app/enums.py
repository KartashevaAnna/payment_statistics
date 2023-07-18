from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class CompanyStatus(ExtendedEnum):
    active = 'active'
    disabled = 'disabled'
    pending_approval = 'pending_approval'
