from typing import Any, List


class BaseSteps(object):
    def __init__(self, created_obj: List[Any]):
        self.created_obj = created_obj