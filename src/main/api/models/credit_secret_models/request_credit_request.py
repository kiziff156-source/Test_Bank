from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class RequestCreditRequest(BaseModel):
    accountId: int
    amount: Annotated[float, CreationRule(min_value=5000, max_value=15000)]
    termMonths: Annotated[int, CreationRule(min_value=1, max_value=12)]