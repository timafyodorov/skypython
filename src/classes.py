from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

class MixinLog(AbstractProduct):
    def __init__(self, name=None, description=None, price=None, quantity=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity
        print(repr(self))

    @property
    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, {self._description}, {self._price}, {self._quantity})"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f"Product: {self._name}, Description: {self._description}, Price: {self._price}, Quantity: {self._quantity}"

class Product(MixinLog):
    def __init__(self, name, description, price, quantity):
        super().__init__(name=name, description=description, price=price, quantity=quantity)

product = Product(name="Example", description="Example Description", price=100, quantity=10)
print(product)
