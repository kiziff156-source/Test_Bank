from src.main.api.models.base_model import BaseModel


class TransferAmountRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float