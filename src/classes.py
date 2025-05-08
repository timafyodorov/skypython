class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}: {self.description}, Цена: {self.price}, Количество: {self.quantity}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, params):
        name = params.get("name")
        description = params.get("description")
        price = params.get("price")
        quantity = params.get("quantity")
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, other):
        if isinstance(other, Product):
            self.__products.append(other)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return self.__products

    def get_products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self):
        return f"{self.name}, количество продуктов: {(sum(p.quantity for p in self.__products))} шт."


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color