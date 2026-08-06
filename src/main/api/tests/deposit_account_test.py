import pytest

from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.models.user_models.deposit_account_request import DepositAccountRequest
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

    @pytest.mark.parametrize(
        "amount",
        [
            999.99,
            9000.01
        ]

    )
    def test_deposit_account_with_invalid_amount(self, api_manager, create_user_request, create_account_request, amount):
        deposit_account_with_invalid_amount = DepositAccountRequest(accountId=create_account_request.id, amount=amount)
        api_manager.user_steps.deposit_account_invalid(create_user_request, deposit_account_with_invalid_amount)