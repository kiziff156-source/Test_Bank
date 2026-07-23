
from asyncio import Protocol
from typing import Optional, Protocol
from requests import Response


from src.main.api.models.base_model import BaseModel
from src.main.api.specs.response_specs import ResponseSpecs


class CrudEndpoint(Protocol):
    def post(self, model: Optional[BaseModel]) -> BaseModel | Response:
       pass
    def get(self, user_id: int) -> BaseModel | Response:
        pass
    def delete(self, user_id: int) -> BaseModel | Response:...