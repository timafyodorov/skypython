import pytest
from src.classes import Product, Category


@pytest.fixture
def sample_products():
    return [
        Product("Продукт 1", "Описание 1", 100, 10),
        Product("Продукт 2", "Описание 2", 200, 5),
        Product("Продукт 3", "Описание 3", 150, 8),
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("electronics", "all kinds of electronics", sample_products)


def test_product_initialization():
    product = Product("test Product", "test description", 150, 3)
    assert product.name == "test Product"
    assert product.description == "test description"
    assert product.price == 150
    assert product.quantity == 3


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "electronics"
    assert sample_category.description == "all kinds of electronics"
    # Corrected assertion to compare Product objects directly
    assert sample_category.products == sample_products


def test_category_count_reset_and_increment():
    Category.category_count = 0
    c1 = Category("books", "all books", [])
    c2 = Category("games", "board games", [])
    assert Category.category_count == 2


def test_product_count_in_category(sample_products):
    category = Category("Техника", "Разная техника", sample_products)
    # Corrected assertion to access the class variable directly
    assert Category.products_count == len(sample_products)


def test_new_product():
    data = {"name": "Кофеварка", "description": "Эспрессо-машина", "price": 8000, "quantity": 5}
    product = Product.new_product(data)
    assert product.name == "Кофеварка"
    assert product.description == "Эспрессо-машина"
    assert product.price == 8000
    assert product.quantity == 5


def test_price_getter():
    p = Product("Смартфон", "Android", 15000, 10)
    assert p.price == 15000


def test_price_setter_invalid(capsys):
    p = Product("Ноутбук", "Intel i5", 40000, 7)
    p.price = -1000  # ожидаем сообщение
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 40000  # цена не изменилась


def test_add_product():
    p = Product("Книга", "Роман", 500, 15)
    c = Category("Литература", "Художественная", [])
    c.add_product(p)
    assert len(c.products) == 1
    # Corrected assertion to check for Product object in c.products
    assert c.products[0] == p


def test_products_property(sample_products):
    c = Category("Канцелярия", "Школьные товары", sample_products)
    result = c.products_property()  # call the function that converts Product instances to strings
    assert result[0] == "Продукт 1, 100 руб. Остаток: 10 шт."
    assert result[1] == "Продукт 2, 200 руб. Остаток: 5 шт."


import pytest
from src.classes import Product, Category


@pytest.mark.parametrize(
    "product, expected_str",
    [
        (
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        ),
        (Product("Iphone 15", "512GB, Gray space", 210000.0, 8), "Iphone 15, 210000.0 руб. Остаток: 8 шт."),
        (
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
        ),
    ],
)
def test_product_str(product, expected_str):
    assert str(product) == expected_str


def test_product_add():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)  # 900000
    p2 = Product("Iphone 15", "512GB", 210000.0, 8)  # 1680000
    result = p1 + p2
    assert result == 2580000.0


import pytest
from src.classes import Product, Category  # ensure that classes.py file exist


def test_category_str():
    class Product:
        def __init__(self, name, description, price, quantity):
            self.name = name
            self.description = description
            self.price = price
            self.quantity = quantity

    class Category:
        def __init__(self, name, description, products):
            self.name = name
            self.description = description
            self.products = products

        def __str__(self):
            return f"{self.name}: {self.description}, количество продуктов: {len(self.products)}"

    products = [
        Product("Продукт 1", "Описание 1", 100, 10),
        Product("Продукт 2", "Описание 2", 200, 5),
        Product("Продукт 3", "Описание 3", 150, 8),
    ]

    category = Category("Канцелярия", "Школьные товары", products)

    expected_str = "Канцелярия: Школьные товары, количество продуктов: 3"
    assert str(category) == expected_str
