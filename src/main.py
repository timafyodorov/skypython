from typing import List

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Товар: {self.name}")
        print(f"Описание: {self.description}")
        print(f"Цена: {self.price} руб.")
        print(f"Количество на складе: {self.quantity} шт.\n")


class Category:
    # Атрибуты класса (общие для всех объектов)
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем общее количество категорий на 1
        Category.total_categories += 1

        # Увеличиваем общее количество товаров на количество товаров в списке
        Category.total_products += len(products)

    def show_products(self):
        print(f"\nКатегория: {self.name}")
        print(f"Описание: {self.description}")
        print("Список товаров:")
        for product in self.products:
            product.show_info()
