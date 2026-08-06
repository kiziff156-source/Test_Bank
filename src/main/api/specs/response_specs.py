from http import HTTPStatus

from requests import Response


class ResponseSpecs:
    @staticmethod
    def request_ok():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.OK, response.text
        return confirm

    @staticmethod
    def request_created():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.CREATED, response.text
        return confirm

    @staticmethod
    def request_bad():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.BAD_REQUEST, response.text
        return confirm

    @staticmethod
    def request_no_more_account():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.CONFLICT, response.text
        return confirm
    @staticmethod
    def request_bad_login():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.UNAUTHORIZED, response.text
        return confirm
    @staticmethod
    def request_insufficient_funds():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT, response.text
        return confirm
    def request_credit_isinstanse():
        def confirm (response: Response):
            assert response.status_code == HTTPStatus.FORBIDDEN, response.text
        return confirm
