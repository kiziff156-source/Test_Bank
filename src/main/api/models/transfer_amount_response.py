from src.main.api.models.base_model import BaseModel


class TransferAmountResponse(BaseModel):
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance: float