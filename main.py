PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5


class RetailItem:
    def __init__(self, description, inventory, price):
        self.__description = description
        self.__inventory = inventory
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price

    def __str__(self):
        result = 'Описание: ' + self.get_description() + '\n' + \
                 'Единиц на складе: ' + str(self.get_inventory()) + \
                 '\nЦена: $' + str(self.get_price())
        return result


class CashRegister:

    def __init__(self):
        self.__item_list = []

    def purchase_item(self, item):
        self.__item_list.append(item)

    def get_total(self):
        sum = 0
        for i in self.__item_list:
            sum += i.get_price()
        return sum

    def show_items(self):
        for i in self.__item_list:
            print(i)

    def clear(self):
        self.__item_list = []

def main():

    # Создать продаваемые товары.
    pants = RetailItem('Брюки', 10, 19.99)
    shirt = RetailItem('Рубашка', 15, 12.50)
    dress = RetailItem('Платье', 3, 79.00)
    socks = RetailItem('Носки', 50, 1.00)
    sweater = RetailItem('Свитер', 5, 49.99)

    # Создать словарь продаваемых товаров.
    sale_items = {PANTS: pants, SHIRT: shirt,
                  DRESS: dress, SOCKS: socks,
                  SWEATER: sweater}

    # Создать кассовый аппарат.
    register = CashRegister()

    # Инициализировать проверку цикла.
    checkout = 'Н'

    # Пользователь хочет приобрести дополнительные товары:
    while checkout == 'Н':

        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print('Этого товара нет в наличии.')
        else:
            register.purchase_item(item)

            # Обновить товарную позицию
            new_item = RetailItem(item.get_description(),
                                         item.get_inventory() - 1,
                                         item.get_price())
            sale_items[user_choice] = new_item

            checkout = input('Вы готовы оформить покупку (Д/Н)? ')

    print()
    print('Сумма Вашей покупки составляет: ',
          format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()


def get_user_choice():
    print('Menu')
    print('---------------------------------')
    print('1. Брюки')
    print('2. Рубашка')
    print('3. Платье')
    print('4. Носки')
    print('5. Свитер')
    print()

    choice = int(input('Введите пункт меню товара, ' +
                       'который вы хотели бы приобрести: '))
    print()

    while choice > SWEATER or choice < PANTS:
        choice = int(input('Введите допустимый номер товара: '))
        print()

    return choice

if __name__ == '__main__':
    main()
