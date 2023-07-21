from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "company" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "org_type" VARCHAR(16),
    "name" VARCHAR(256),
    "inn" VARCHAR(15),
    "current_account" VARCHAR(20),
    "activity" VARCHAR(256),
    "logo_url" VARCHAR(256),
    "email" VARCHAR(128),
    "phone_number" VARCHAR(11),
    "status" VARCHAR(16) NOT NULL,
    "is_sanctioned" BOOL,
    "site_url" VARCHAR(256)
);
COMMENT ON COLUMN "company"."status" IS 'active: active\ndisabled: disabled\npending_approval: pending_approval';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
