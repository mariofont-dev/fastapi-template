# database.py
from sqlmodel import SQLModel, create_engine, Session

# Import models so SQLModel knows about them
from app.config.settings import settings
from app.contexts.user.infrastructure.persistence.sql.models.user import User

DATABASE_URL = settings.sqlite_url

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Print SQL for debugging
    connect_args={"check_same_thread": False},  # Needed only for SQLite
)


def get_session():
    with Session(engine) as session:
        yield session
