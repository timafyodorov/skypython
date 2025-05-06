class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):  # 15.1
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):  # 15.1
        res = self.__price * self.quantity + other.__price * other.quantity
        return res

    @classmethod  # 14.2
    def new_product(cls, product: dict):
        return cls(
            product["name"],
            product["description"],
            product["price"],
            product["quantity"],
        )

    @property  # 14.2
    def price(self):
        return self.__price

    @price.setter  # 14.2
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list["Product"]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.products_count = len(products)

    def __str__(self):  # 15.1
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):  # 14.2
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property  # 14.2
    def products(self):
        result = []
        for product in self.__products:
            result.append(str(product))
        return result

    class Product:
        name: str
        description: str
        price: int
        quantity: int

        def __init__(self, name, description, price, quantity):
            self.name = name
            self.description = description
            self.__price = price
            self.quantity = quantity

        def __str__(self):  # 15.1
            return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

        def __add__(self, other):  # 15.1
            res = self.__price * self.quantity + other.__price * other.quantity
            return res

        @classmethod  # 14.2
        def new_product(cls, product: dict):
            return cls(
                product["name"],
                product["description"],
                product["price"],
                product["quantity"],
            )

        @property  # 14.2
        def price(self):
            return self.__price

        @price.setter  # 14.2
        def price(self, new_price):
            if new_price <= 0:
                print("Цена не должна быть нулевая или отрицательная")
            else:
                self.__price = new_price

    class Category:
        category_count = 0
        product_count = 0
        name: str
        description: str
        products: list["Product"]

        def __init__(self, name, description, products):
            self.name = name
            self.description = description
            self.__products = products
            Category.category_count += 1
            Category.products_count = len(products)

        def __str__(self):  # 15.1
            total_quantity = sum(product.quantity for product in self.__products)
            return f"{self.name}, количество продуктов: {total_quantity} шт."

        def add_product(self, product):  # 14.2
            if isinstance(product, Product):
                self.__products.append(product)
                Category.product_count += 1

        @property  # 14.2
        def products(self):
            result = []
            for product in self.__products:
                result.append(str(product))
            return result

    if __name__ == "__main__":
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print(str(product1))
    print(str(product2))
    print(str(product3))
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    print(str(category1))
    print(category1.products)
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
