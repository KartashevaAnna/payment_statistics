import fastapi
import loguru
import uvicorn

from app.db_config import db_config
from app.routes.company import company_router, company_fake_router
from app.routes.healthcheck import ping_router
from app.schemas.mock import Mock
from utils.helpers import get_fake_company
from utils.logger import setup_logging
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


def build_app(logger) -> fastapi.FastAPI:
    app = fastapi.FastAPI(
        title="Payment statistics",
        description="Payment statistics app",
        version="1.0",
        openapi_url="/api/v1/openapi.json",
        docs_url="/api/v1/docs",
        redoc_url="/api/v1/redoc",
        logger=logger,
    )

    app.include_router(ping_router)
    app.include_router(company_router)
    app.include_router(company_fake_router)

    app.state.mock: Mock = Mock(companies=[get_fake_company() for _ in range(10)])

    register_tortoise(
        app,
        config=db_config,
    )

    return app


def main():
    logger = setup_logging(loguru.logger)
    uvicorn.run(build_app(logger), host="localhost", port=8000)


if __name__ == "__main__":
    main()
