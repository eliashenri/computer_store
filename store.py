from typing import List, Dict
from time import sleep

from models.item import Item
from utils.helper import format_float_str_currency


items: list[Item] = []
basket: list[dict[Item, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('=========================')
    print('======== Welcome ========')
    print('===== Hardware Shop =====')
    print('=========================')

    print('Select a below option')
    print('1 - Register Items')
    print('2 - List Items')
    print('3 - Purchase Items')
    print('4 - Basket View')
    print('5 - Close Order')
    print('6 - Exit')

    option: int = int(input())

    if option ==1:
        item_register()
    elif option == 2:
        items_list()
    elif option == 3:
        item_purchase()
    elif option ==4:
        basket_view()
    elif option ==5:
        close_order()
    elif option == 6:
        print('See you soon')
        sleep(3)
        exit(0)
    else:
        print('Invalid Option')
        sleep(1)
        menu()

def item_register() -> None:
    print('Register Items')
    print('==============')

    name: str = input('Insert the item name: ')
    price: float = float(input('Insert the Item price: '))

    item: Item = Item(name, price)

    items.append(item)

    print(f'The Item {item.name} has sucess reigster')
    sleep(3)
    menu()

def item_list() -> None:
    if len(item) > 0:
        print('Items List')
        print('==========')
        for item in items
        print(item)
        print('===============')
        sleed(1)
    else:
        print('No one item are register yet')
        sleep(3)
        menu()

def item_purchase() -> None:
    if len(items) > 0:
        print('Enter the code of the item, to add it in your basket')
        print('====================================================')
        print('================== Items on Sale ===================')
        for item in items:
            print(item)
            print('====================================================')
            sleep(1)
        code: int = int(input())

        item: Item = get_item_from_code(code)

        if item:
            if len(basket) > 0:
                have_in_basket: bool = False
                for item in basket:
                    amount: int = product.get(items)
                    if amount:
                        product[item] = amount + 1
                        print)f'The Item {item.name} now have {amount + 1} units in the basket'
                        have_in_basket = True
                        sleep(3)
                        menu()
                if not have_in_basket:
                    prod = {item: 1}
                    basket.append(prod)
                    print)f'The Item {item.name} has add in the basket'
                    sleep(3)
                    menu()
            else:
                product = {item = 1}
                basket.append(product)
                print(f'The Item {item.name} has add to the basket')
                sleep(3)
                menu()
        else:
            product = {item: 1}
            basket.append(product)
            print(f'No one item with the code: {code} was found')
            sleep(3)
            menu()
    else:
        print(f'All the items are out of stock')
        sleep(3)
        menu()

def basket_view() -> None:
    if len(basket) > 0:
        print('Items in the basket: ')

        for Item in basket
            for data in item.items
            print(data[])
            print(f'Amount: {data[1]})
            print('================')
            sleep(1)

    else:
        print('Yours basket is empty')
        sleep(3)
        menu()

def close_order() -> None:
    if len(items) > 0:
        total_value: float = 0

        print('Items in Basket')
        for item in basket:
            for data in item.items()
            print(data[0])
            print(f'Amount: {data[1]}')
            total_value += data[0].price * data[1]
            print('=====================')
            sleep(1)
        print(f'Yours total invoice is {format_float_str_currency(total_value)}')
        print('See you soon')
        basket.clear()
        sleep(5)
    else:
        print('Yours basket is empty')
    sleep(3)
    menu()

def get_item_from_code(code: int) -> Item:
    i: item = None

    for item in items:
        if item.code == code:
            p = item
    return p


if __name__ = '__main__':
    main()  
