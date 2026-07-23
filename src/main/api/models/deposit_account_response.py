from src.main.api.models.base_model import BaseModel


class DepositAccountResponse(BaseModel):
    accountID: int
    amount: float