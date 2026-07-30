import pytest

from src.main.api.fixtures.api_fixtures import api_manager


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, api_manager, create_user_request):

        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0


    def test_create_account_second(self, api_manager, create_user_request, create_account_request):
        account_response = create_account_request
        second_account_response = api_manager.user_steps.create_account(create_user_request)

        assert second_account_response.balance == 0
        assert second_account_response.id != account_response.id
        assert second_account_response.number != account_response.number