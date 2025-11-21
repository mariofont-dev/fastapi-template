from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    sqlite_url: str = Field(default="sqlite:///./app.db")


settings = Config()
