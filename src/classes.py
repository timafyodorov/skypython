from abc import ABC, abstractmethod
from typing import List, Dict


class BaseProduct(ABC):
    @abstractmethod
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict[str, any]) -> 'BaseProduct':
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class PrintInitMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ", ".join(
            [f"{arg!r}" for arg in args] +
            [f"{k}={v!r}" for k, v in kwargs.items()]
        )
        print(f"Создан объект {class_name}({params})")
        super().__init__(*args, **kwargs)


class Product(PrintInitMixin, BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену, если она положительная."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict[str, any]) -> 'Product':
        """Создает продукт из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """Суммирует произведения цены на количество."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return (
            (self.__price * self.quantity) +
            (other.__price * other.quantity)
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    _Category__products: None
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product] = None
    ):
        self._Category__products = None
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только Product или подклассы")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с продуктами, используя их __str__."""
        return "".join(str(product) + "\n" for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."