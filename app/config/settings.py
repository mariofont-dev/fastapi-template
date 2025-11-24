from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    sqlite_url: str = Field(
        default="sqlite:///./app.db",
        description="SQLite database URL (fallback)",
    )

    @property
    def database_url(self) -> str:
        """Get the main database URL"""
        return self.sqlite_url


settings = Config()
