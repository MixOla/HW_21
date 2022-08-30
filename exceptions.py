class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(BaseError):
    message = 'Не хватает на складе, попробуйте заказать меньше'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequest(BaseError):
    message = 'Неправильный запрос. Попробуйте снова'


class InvalidStorageName(BaseError):
    message = 'Введен несуществующий склад'
