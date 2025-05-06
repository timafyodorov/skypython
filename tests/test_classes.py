import pytest
from src.classes import Product, Category


@pytest.fixture
def sample_products():
    return [
        Product("Продукт 1", "Описание 1", 100, 10),
        Product("Продукт 2", "Описание 2", 200, 5),
        Product("Продукт 3", "Описание 3", 150, 8)
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


def test_category_initialization(sample_category, expected_str=None):
    assert str(sample_category) == expected_str


def test_new_product():
    data = {
        "name": "Кофеварка",
        "description": "Эспрессо-машина",
        "price": 8000,
        "quantity": 5
    }
    product = Product.new_product(data)
    assert product.name == "Кофеварка"
    assert product.description == "Эспрессо-машина"
    assert product.price == 8000
    assert product.quantity == 5


def test_price_setter_invalid(capsys):
    product = Product("Ноутбук", "Intel i5", 40000, 7)
    product.price = -1000  # Expecting a message
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 40000  # Price should not change
    # Test for adding two products together


def test_product_add():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB", 210000.0, 8)
    total_price = p1.price * p1.quantity + p2.price * p2.quantity
    assert total_price == 2580000.0
