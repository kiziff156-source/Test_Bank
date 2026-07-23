
from src.main.api.models.base_model import BaseModel

class AccountDepositRequest(BaseModel):
    accountID: int
    amount: float