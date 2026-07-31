from src.main.api.models.base_model import BaseModel
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule

class TransferAmountRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float