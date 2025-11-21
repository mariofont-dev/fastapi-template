from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    sqlite_url: str = Field(
        default="sqlite:///./app.db",
        description="Database URL (supports SQLite and PostgreSQL)",
    )

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Config()
