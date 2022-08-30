from typing import Dict

from entity.abstract_storage import AbstractStorage
# from main import storages
from request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.to in storages:
            self.__to = storages[self.__request.to]

    def move(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} со {self.__request.departure}')
        print(
            f'Курьер везет {self.__request.amount} {self.__request.product} со {self.__request.departure} в {self.__request.to}')

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.to}')
