import fastapi
import loguru
import uvicorn

from app.routes.company import company_router
from app.routes.healthcheck import ping_router
from utils.logger import setup_logging


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

    return app


def main():
    logger = setup_logging(loguru.logger)
    uvicorn.run(build_app(logger), host="localhost", port=8000)


if __name__ == "__main__":
    main()
