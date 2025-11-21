from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    sqlite_url: str = Field(
        default="sqlite:///./app.db",
        description="SQLite database URL (fallback)",
    )

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def database_url(self) -> str:
        """Get the main database URL"""
        return self.sqlite_url


settings = Config()
