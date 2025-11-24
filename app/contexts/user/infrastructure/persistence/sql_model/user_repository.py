from uuid import UUID

from sqlmodel import select
from app.contexts.user.domain.entities.user_entity import UserEntity
from app.contexts.user.domain.persistence.user_repository import UserRepositoryInterface
from app.contexts.user.infrastructure.persistence.sql_model.models.user import User
from app.shared.infrastructure.database.connection import DatabaseConnection


class SQLModelRepository(UserRepositoryInterface):

    def __init__(self, database: DatabaseConnection):
        self.database = database

    def create(self, user: UserEntity) -> UserEntity:
        user_model = User(
            id=str(user.id),
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
        )

        with self.database.get_session() as session:
            session.add(user_model)
            session.commit()

        return user

    def get_by_id(self, identifier: UUID) -> UserEntity:
        query = select(User)
        query = query.where(User.id == str(identifier))

        with self.database.get_session() as session:
            result = session.exec(query).first()

        if result is None:
            raise ValueError("User not found")

        return UserEntity(
            id=UUID(result.id),
            first_name=result.first_name,
            last_name=result.last_name,
            age=result.age,
        )
