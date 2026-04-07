Модуль для работы с корзиной покупок.
items = []

def add_item(name, price):
    """Добавить товар в корзину."""
    item = {'name': name, 'price': price}
    items.append(item)


def get_total_price():
    """Вернуть суммарную стоимость всех товаров."""
    total = 0
    for item in items:
        total = total + item['price']
    return total


def print_receipt():
    """Вывести чек на экран."""
    print("=== Чек ===")
    for item in items:
        print(item['name'], item['price'])
    total = get_total_price()
    print("Итого:", total)


if __name__ == "__main__":
    add_item("Хлеб", 45)
    add_item("Молоко", 89)
    add_item("Масло", 120)
    print_receipt()