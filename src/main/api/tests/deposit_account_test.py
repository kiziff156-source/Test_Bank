import pytest
from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse
from src.main.api.models.user_models.deposit_account_request import DepositAccountRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.db.crud.account_crud import AccountCRUD as Account


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_request:CreateAccountResponse
    ):
        generated_amount_request = RandomModelGenerator.generate(DepositAccountRequest,accountId=create_account_request.id)
        deposit_account_response = api_manager.user_steps.deposit_account(create_user_request, generated_amount_request)

        balance_from_db = Account.get_balance_by_account_id(db_session, generated_amount_request.accountId)

        assert generated_amount_request.accountId == deposit_account_response.id
        assert generated_amount_request.amount == deposit_account_response.balance

        assert generated_amount_request.amount == balance_from_db.balance, f"Account '{generated_amount_request.accountId}' not deposited"

    @pytest.mark.parametrize(
        "amount",
        [
            999.99,
            9000.01
        ]

    )
    def test_deposit_account_with_invalid_amount(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_request:CreateAccountResponse,
            amount
    ):
        deposit_account_with_invalid_amount = DepositAccountRequest(accountId=create_account_request.id, amount=amount)
        api_manager.user_steps.deposit_account_invalid(create_user_request, deposit_account_with_invalid_amount)

        balance_from_db = Account.get_balance_by_account_id(db_session, deposit_account_with_invalid_amount.accountId)

        assert balance_from_db.balance == 0.0, f"Account '{create_account_request.id}' deposited. Balance '{balance_from_db.balance}'"