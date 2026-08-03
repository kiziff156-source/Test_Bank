import pytest

@pytest.mark.api
class TestCreateAccountCredit:
    def test_create_account_credit(self, api_manager,create_credit_secret):
        response = api_manager.credit_steps.create_account_credit(create_credit_secret)
        assert response.balance == 0
