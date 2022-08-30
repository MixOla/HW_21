from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < int(amount):
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += int(amount)
        else:
            self.__items[name] = int(amount)

    def remove(self, name: str, amount: int) -> None:
        if name not in self.__items or self.__items[name] < int(amount):
            raise NotEnoughProduct
        print("Нужное количество есть на складе")
        self.__items[name] -= int(amount)
        if self.__items[name] == 0:
            self.__items.pop(name)


    def get_free_space(self) -> int:
        current_space = 0
        for value in self.__items.values():
            current_space += value

        return self.__capacity - current_space


    def get_items(self) -> Dict:
        return self.__items


    def get_unique_items_count(self) -> int:
        return len(self.__items)