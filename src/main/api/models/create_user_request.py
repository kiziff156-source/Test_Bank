from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class CreateUserRequest(BaseModel):
    username: Annotated[str, CreationRule(regex=r'^[A-Za-z0-9]{3,15}$')]
    password: Annotated[str, CreationRule(regex=r'^[A-Z][a-z]\d[!@#$%^&*][A-Za-z\d!@#$%^&*]{4}$')]
    role: str
