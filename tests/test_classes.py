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

import unittest

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(name="Test Product", description="Test Description", price=50, quantity=5)

    def test_initialization(self):
        self.assertEqual(self.product._name, "Test Product")
        self.assertEqual(self.product._description, "Test Description")
        self.assertEqual(self.product._price, 50)
        self.assertEqual(self.product._quantity, 5)

    def test_price_property(self):
        self.assertEqual(self.product.price, 50)
        self.product.price = 75
        self.assertEqual(self.product.price, 75)

    def test_str_method(self):
        expected_str = "Product: Test Product, Description: Test Description, Price: 50, Quantity: 5"
        self.assertEqual(str(self.product), expected_str)

    def test_repr_method(self):
        expected_repr = "Product(Test Product, Test Description, 50, 5)"
        self.assertEqual(repr(self.product), expected_repr)

if __name__ == '__main__':
    unittest.main()
