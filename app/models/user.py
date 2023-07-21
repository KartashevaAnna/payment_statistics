from tortoise import fields, models

from app.enums import UserStatus, UserRole


class User(models.Model):
    id = fields.UUIDField(pk=True)
    first_name = fields.CharField(max_length=128)
    last_name = fields.CharField(max_length=128)
    email = fields.CharField(max_length=128)
    password = fields.BinaryField()
    status = fields.CharEnumField(UserStatus)
    role = fields.CharEnumField(UserRole)
    company_id = fields.UUIDField()

    class Meta:
        table = "user"
        db_schema = "payment_statistics"
        app = 'payment_statistics'

__models__ = [User]