import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.db.crud.user_crud import UserCrudDb as User


@pytest.mark.api
class TestCreateCreditSecret:
    @pytest.mark.parametrize(
        "generated_credit_secret",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_credit_secret(
            self,
            db_session:Session,
            api_manager:ApiManager,
            generated_credit_secret
    ):
        generated_credit_secret.role = "ROLE_CREDIT_SECRET"
        response = api_manager.admin_steps.create_user(generated_credit_secret)
        assert generated_credit_secret.username == response.username
        assert generated_credit_secret.role == response.role

        user_from_db = User.get_user_by_username(db_session, generated_credit_secret.username)
        assert user_from_db.username == generated_credit_secret.username, 'User not exist, error'

    @pytest.mark.parametrize(
        "password",
        [
            "Pas!sw0rд"
            "Pas!sw0",
            "PAS!SW0RD",
            "Passsw0rd",
            "Pas!sword"
        ]
    )
    def test_create_credit_secret_invalid_password (
            self,
            db_session: Session,
            api_manager:ApiManager,
            password):
        create_credit_secret_invalid_password = CreateUserRequest(username= "Max", password=password, role= "ROLE_CREDIT_SECRET")
        api_manager.admin_steps.create_invalid_user(create_credit_secret_invalid_password)

        user_from_db = User.get_user_by_username(db_session, create_credit_secret_invalid_password.username)
        assert user_from_db is None, 'User already exists, error'

    @pytest.mark.parametrize(
        "username",
            [
                "абв",
                "ab",
                "ab!"
            ]
        )
    def test_create_credit_secret_invalid_username(
            self,
            db_session: Session,
            api_manager:ApiManager,
            username):
        create_credit_secret_invalid_username = CreateUserRequest(username=username, password="Pas!sw0rd",role="ROLE_CREDIT_SECRET")
        api_manager.admin_steps.create_invalid_user(create_credit_secret_invalid_username)

        user_from_db = User.get_user_by_username(db_session, create_credit_secret_invalid_username.username)
        assert user_from_db is None, 'User already exists, error'
