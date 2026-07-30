import pytest

from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.models import create_user_response
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestDepositAccount:
    @pytest.mark.parametrize(
        "generated_amount",
        [RandomModelGenerator.generate(DepositAccountRequest)],
    )
    def test_deposit_account(self, api_manager, create_user_request, create_account_request,generated_amount):
        generated_amount.accountId = create_account_request.id
        deposit_account_response = api_manager.user_steps.deposit_account(create_user_request, generated_amount)

        assert generated_amount.accountId == deposit_account_response.id
        assert generated_amount.amount == deposit_account_response.balance