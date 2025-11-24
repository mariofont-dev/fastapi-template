from sqlmodel import create_engine, Session

from app.shared.infrastructure.database.connection import DatabaseConnection


class SQLModelConnection(DatabaseConnection):
    def __init__(self, database_url: str):
        self.engine = create_engine(
            database_url,
            echo=True,  # Print SQL for debugging
            connect_args={"check_same_thread": False},
        )

    def get_session(self) -> Session:
        return Session(self.engine)
