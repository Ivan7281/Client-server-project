from typing import ClassVar, List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = 'search_su'
    POSTGRES_HOST: str = '127.0.0.1'
    POSTGRES_PASSWORD: str = '654321'
    POSTGRES_DB: str = 'search_db'
    POSTGRES_PORT: str = '5439'
    PG_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    DATABASE_URL: str = ''
    DB_DICT: dict = {}

    LOG_LEVEL: str = "INFO"
    DEBUG: bool = True

    LOG_CONFIG: ClassVar = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {"default": {"format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s"}},
        "handlers": {
            "console": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "level": LOG_LEVEL,
            }
        },
        "root": {"handlers": ["console"], "level": LOG_LEVEL},
        "loggers": {
            "gunicorn": {"propagate": True},
            "gunicorn.access": {"propagate": True},
            "gunicorn.error": {"propagate": True},
            "uvicorn": {"propagate": True},
            "uvicorn.access": {"propagate": True},
            "uvicorn.error": {"propagate": True},
            "sqlalchemy.engine": {"propagate": True},
        },
    }

    class Config:
        case_sensitive = True
        env_file = "../../.env"
        env_file_encoding = "utf-8"


settings = Settings()


