from uuid import UUID, uuid4

from pydantic import Field

from app.shared.domain.entities.custom_base_model import CustomBaseModel


class User(CustomBaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    age: int
