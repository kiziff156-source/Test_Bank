from typing import Any,List

import pytest

from src.main.api.classes.api_manager import ApiManager


@pytest.fixture
def api_manager(create_obj: List[Any]):
    return ApiManager(create_obj)