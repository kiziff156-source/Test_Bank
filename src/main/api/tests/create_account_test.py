import pytest
from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse
from src.main.api.db.crud.account_crud import AccountCRUD as Account


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest
            ):

        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id, 'Account not created in DataBase, error'
        assert account_from_db.balance is not None, 'Balance not created in DataBase, error'


    def test_create_account_second(
            self,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_request:CreateAccountResponse
            ):
        account_response = create_account_request
        second_account_response = api_manager.user_steps.create_account(create_user_request)

        assert second_account_response.balance == 0
        assert second_account_response.id != account_response.id
        assert second_account_response.number != account_response.number

    def test_create_account_third_invalid(
            self, api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_second:CreateAccountResponse
    ):
        api_manager.user_steps.create_account_invalid(create_user_request)
