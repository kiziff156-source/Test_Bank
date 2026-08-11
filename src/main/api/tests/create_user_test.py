import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.user_fixtures import create_user_request
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.db.crud.user_crud import UserCrudDb as User


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "generated_user",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user_valid(
            self,
            api_manager:ApiManager,
            generated_user,
            db_session:Session
    ):
        generated_user.role = "ROLE_USER"
        response = api_manager.admin_steps.create_user(generated_user)

        assert generated_user.username == response.username
        assert generated_user.role == response.role

        user_from_db = User.get_user_by_username(db_session, generated_user.username)
        assert user_from_db.username == generated_user.username, 'User not exist, error'

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("ab!", "Pas!sw0rd"),
            ("Maxx1", "Pas!sw0rд"),
            ("Maxx2", "Pas!sw0"),
            ("Maxx3", "pas!sw0rd"),
            ("Maxx4", "PAS!SW0RD"),
            ("Maxx5", "Passsw0rd"),
            ("Maxx6", "Pas!sword")
        ]
    )

    def test_create_user_invalid(
            self,
            db_session:Session,
            username,
            password,
            api_manager:ApiManager
    ):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")

        api_manager.admin_steps.create_invalid_user(create_user_request)
        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, 'User already exists, error'

