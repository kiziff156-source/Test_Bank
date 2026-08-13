import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse
from src.main.api.db.crud.account_crud import AccountCRUD as Account
from src.main.api.db.crud.user_crud import UserCrudDb



@pytest.mark.api
class TestCreateAccountCredit:
    def test_create_account_credit(
            self,
            db_session:Session,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest
            ):
        response = api_manager.credit_steps.create_account_credit(create_credit_secret)
        assert response.balance == 0

        account_credit_from_db = Account.get_account_by_id(db_session,response.id)
        assert account_credit_from_db.id == response.id , f'User Id={response.id} not exist, error'

    def test_create_account_credit_second(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest,
            create_credit_account:CreateAccountResponse
    ):
        credit_account=create_credit_account
        credit_account_second_response = api_manager.credit_steps.create_account_credit(create_credit_secret)

        assert credit_account_second_response.balance == 0
        assert credit_account_second_response.id != credit_account.id
        assert credit_account_second_response.number != credit_account.number

        second_account_credit_from_db = Account.get_account_by_id(db_session,credit_account_second_response.id)
        assert second_account_credit_from_db.id == credit_account_second_response.id , f'User Id={credit_account_second_response.id} not exist, error'

    def test_create_credit_account_third_invalid (
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest,
            create_credit_account_second:CreateAccountResponse
    ):
        api_manager.credit_steps.create_account_credit_invalid(create_credit_secret)

        user = UserCrudDb.get_user_by_username(db_session, create_credit_secret.username)
        accounts = Account.get_accounts_by_user_id(db_session, user.id)

        assert len(accounts) <= 2, (
            f"user '{create_credit_secret.username}' has {len(accounts)} accounts (max 2). "
            f"Accounts: {[a.id for a in accounts]}"
        )






