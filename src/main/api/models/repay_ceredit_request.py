from typing import Optional

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class RepayCreditRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float
    