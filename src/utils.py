import json


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Метод для создания нового продукта из словаря"""
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверкой на допустимость значений."""
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной.")
        elif new_price < self.__price:
            ans = input("Новая цена ниже старой, вы уверены в изменении цены (y/n)? ")
            if ans.lower() == "y":
                self.__price = new_price
            else:
                print("Изменения не применены.")
        else:
            self.__price = new_price


class Category:
    categotries_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Добавляемый объект не является продуктом")

    @property
    def products(self) -> str:
        result = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        ]
        return "\n".join(result)


def read_json(file_path: str) -> list[Category]:
    """Функция для чтения JSON-файла и создания списка категорий"""
    categories = []
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        for i in data:
            name = i["name"]
            description = i["description"]
            products_data = i["products"]

            products = [Product(**product) for product in products_data]
            category = Category(name, description, products)
            categories.append(category)

    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON файла.")
    return categories


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)

    # Добавляем новый продукт в категорию
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(f"Общее количество продуктов: {Category.product_count}")

    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    new_product = Product.new_product(new_product_data)
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)

    new_product.price = 0
    print(new_product.price)
