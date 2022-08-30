from entity.shop import Shop
from entity.store import Store
from entity.courier import Courier
from exceptions import InvalidRequest, BaseError, InvalidStorageName
from request import Request

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "елка": 25
})

shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "елка": 2
})

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f"В {storage_name} хранится:\n")
            for key, value in storages[storage_name].get_items().items():
                print(value, key)
            print()

        user_input = input(
            'Введите запрос в формате: "Доставить 3 печенька из склад в магазин"\n'
            'Введите "stop" или "стоп", если хотите закончить ввод:\n'
        )

        if user_input in ("stop", "стоп"):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except (InvalidRequest, InvalidStorageName) as e:
            print(e.message)
            continue

        courier = Courier(
            request=request,
            storages=storages,
        )

        try:
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
