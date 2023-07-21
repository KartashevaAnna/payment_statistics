from tortoise import fields, models

from app.enums import CompanyStatus


class Company(models.Model):
    id = fields.UUIDField(pk=True)
    org_type = fields.CharField(min_length=2, max_length=16, null=True)
    name = fields.CharField(max_length=256, null=True)
    inn = fields.CharField(min_length=9, max_length=15, null=True)
    current_account = fields.CharField(min_length=9, max_length=20, null=True)
    activity = fields.CharField(max_length=256, null=True)
    logo_url = fields.CharField(max_length=256, null=True)
    email = fields.CharField(max_length=128, null=True)
    phone_number = fields.CharField(min_length=11, max_length=11, null=True)
    status = fields.CharEnumField(enum_type=CompanyStatus)
    is_sanctioned = fields.BooleanField(null=True)
    site_url = fields.CharField(max_length=256, null=True)

    class Meta:
        table = "company"
        db_schema = "payment_statistics"
        app = 'payment_statistics'


__models__ = [Company]
