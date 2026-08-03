from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.request_credit_request import RequestCreditRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class CreditSteps(BaseSteps):
    def create_account_credit(self, create_credit_secret:CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_secret.username, password=create_credit_secret.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_request_credit (self,request_credit_request:RequestCreditRequest,create_credit_secret ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_secret.username, password=create_credit_secret.password),
            Endpoint.REQUEST_CREDIT,
            ResponseSpecs.request_created()
        ).post(request_credit_request)
        return response

