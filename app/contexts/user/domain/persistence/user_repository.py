from abc import ABC, abstractmethod
from uuid import UUID

from app.contexts.user.domain.entities.user_entity import UserEntity
from app.contexts.user.infrastructure.persistence.sql_model.models.user import User


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_id(self, identifier: UUID) -> UserEntity:
        pass
