from utils.helper import format_float_str_currency

class Item:
    count: int = 1

    def __init__(self, name: str, price: float) -> None:
        self.__code: int = Item.count
        self.__name: str = name
        self.__price: float = price
        Item.count += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Code: {self.code} \nName: {self.name} \nPrice: {format_float_str_currency(self.price)}'