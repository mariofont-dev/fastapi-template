

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "user"
    id: str = Field(primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    age: int = Field()
