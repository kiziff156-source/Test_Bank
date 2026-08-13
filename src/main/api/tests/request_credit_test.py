import pytest
from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.credit_secret_models.request_credit_request import RequestCreditRequest
from src.main.api.models.credit_secret_models.request_credit_response import RequestCreditResponse
from src.main.api.models.user_models.create_account_response import CreateAccountResponse
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.db.crud.account_crud import AccountCRUD as Account



@pytest.mark.api
class TestRequestCredit:
    def test_request_credit(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest,
            create_credit_account:CreateAccountResponse
    ):
        request_credit_request=RandomModelGenerator.generate(RequestCreditRequest,accountId=create_credit_account.id)


        response = api_manager.credit_steps.create_request_credit(request_credit_request, create_credit_secret)

        assert request_credit_request.amount == response.amount
        assert request_credit_request.termMonths == response.termMonths

        credit_secret_from_db = Credit.get_credit_from_db_by_account_id(db_session,request_credit_request.accountId)
        account_balance_from_db = Account.get_balance_by_account_id(db_session,request_credit_request.accountId)

        assert credit_secret_from_db.balance == -request_credit_request.amount,  \
    f'Credit DB record mismatch for accountId={request_credit_request.accountId}: ' \
    f'expected={request_credit_request.amount}, actual={credit_secret_from_db.balance}'
        assert account_balance_from_db.balance == request_credit_request.amount, \
    f'Account DB record mismatch for accountId={request_credit_request.accountId}: ' \
    f'expected={request_credit_request.amount}, actual={account_balance_from_db.balance}'


    @pytest.mark.xfail (reason="wrong HTTPStatus_code, expected-403 actual-404")
    def test_request_credit_invalid(
            self,
            db_session: Session,
            api_manager:ApiManager,
            request_credit:RequestCreditResponse,
            create_credit_secret:CreateUserRequest,
            create_credit_account:CreateAccountResponse
    ):
        request_credit_request = RandomModelGenerator.generate(RequestCreditRequest, accountId=create_credit_account.id )

        api_manager.credit_steps.create_request_credit_invalid(request_credit_request, create_credit_secret)

        credits_from_db = Credit.get_credits_from_db_by_account_id(db_session, create_credit_account.id)
        assert len(credits_from_db) <= 1, f"credit-secret {create_credit_secret.username} has {len(credits_from_db)} credits (max 1)"



