from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import InvalidRequest, InvalidStorageName


class Request:
    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        splited_request = request.lower().split(' ')
        if len(splited_request) != 7:
            raise InvalidRequest

        self.departure = splited_request[4]
        self.to = splited_request[6]
        self.amount = splited_request[1]
        self.product = splited_request[2]

        if self.departure not in storages or self.to not in storages:
            raise InvalidStorageName
