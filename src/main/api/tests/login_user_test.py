
import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.db_fixtures import db_session
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.db.crud.user_crud import UserCrudDb as User


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(
            self,
            api_manager:ApiManager,
            db_session:Session
    ):
        login_user_request = LoginUserRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)

        user_from_db = User.get_user_by_username(db_session, login_user_request.username)

        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"
        assert user_from_db.username == login_user_request.username, 'Admin not exist, error'

    def test_login_user(
            self,
            api_manager:ApiManager,
            create_user_request,
            db_session:Session
    ):
        response = api_manager.admin_steps.login_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert create_user_request.username == response.user.username
        assert response.user.role == "ROLE_USER"
        assert user_from_db.username == create_user_request.username, 'User not exist, error'

    def test_invalid_credentials (
            self,
            api_manager:ApiManager,
            db_session: Session
    ):
        unregistered_login = RandomModelGenerator.generate(CreateUserRequest)
        api_manager.user_steps.login_unregistered(unregistered_login)
        user_from_db = User.get_user_by_username(db_session, unregistered_login.username)

        assert user_from_db is None, 'User already exists, error'

