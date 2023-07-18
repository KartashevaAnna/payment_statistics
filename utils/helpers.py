import random
import uuid

from faker import Faker

from app.enums import CompanyStatus
from app.schemas.company import OKVED, CompanySchema
from utils.OKVED_codes_and_descriptions import OKVED_codes_and_descriptions


def get_okved(activity_code):
    if activity_code < 10:
        activity_code = '0' + str(activity_code)
    else:
        activity_code = str(activity_code)
    return OKVED(code=activity_code, description=OKVED_codes_and_descriptions[activity_code])


def get_fake_company():
    fake = Faker(locale='ru_RU')
    mock_data = {
        'id': uuid.uuid4(),
        'org_type': fake.company_prefix(),
        'name': fake.name(),
        'inn': fake.individuals_inn(),
        'current_account': fake.checking_account(),
        'activity': get_okved(random.randint(1, len(OKVED_codes_and_descriptions))),
        'logo_url': fake.image_url(),
        'email': fake.safe_email(),
        'phone_number': fake.phone_number(),
        'status': random.choices(CompanyStatus.list())[0],
        'is_sanctioned': random.choice([True, False]),
        'site_url': fake.url(),
    }
    return CompanySchema(**mock_data)
