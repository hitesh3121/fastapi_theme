from fastapi import FastAPI, HTTPException
from uvicorn import Config, Server
from src.common.error_handler import http_error_handler
from src.database.database import Base, engine
from src.routers.api import router as api_route
from src.common.logger import setup_logging, LOG_LEVEL

def get_application() -> FastAPI:
    applications = FastAPI()
    Base.metadata.create_all(bind=engine)
    applications.include_router(api_route, prefix='/api')
    applications.add_exception_handler(HTTPException, http_error_handler)
    setup_logging()
    return applications


app = get_application()


if __name__ == "__main__":
    server = Server(
        Config(
            "main:app",
            host="0.0.0.0",
            log_level=LOG_LEVEL,
        ),
    )
    server.run()
