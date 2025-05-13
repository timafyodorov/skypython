import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def category(products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [products[0], products[1], products[2]],
    )


@pytest.fixture
def grasses():
    return [
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый"),
        LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый"),
    ]


@pytest.fixture
def smartphones():
    return [
        Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        ),
        Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"),
    ]


def test_product_initialization(products):
    product = products[0]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(products):
    category = Category("Смартфоны", "Описание категории", products)
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_product_count(products):
    Category("Смартфоны", "Описание категории", products)
    assert Category.product_count == 3

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category("Телевизоры", "Описание категории", [product4])
    assert Category.product_count == 4


def test_category_count(products):
    Category("Смартфоны", "Описание категории", products)
    assert Category.category_count == 1

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category("Телевизоры", "Описание категории", [product4])
    assert Category.category_count == 2


def test_product_price_getter_setter():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.price == 100.0

    product.price = 150.0
    assert product.price == 150.0


def test_new_product():
    params = {"name": "Test Product", "description": "Description", "price": 100.0, "quantity": 10}
    product = Product.new_product(params)

    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_add_product(products):
    category = Category("Смартфоны", "Описание категории", products)
    initial_product_count = len(category.products)

    new_product = Product("Google Pixel 7", "128GB, Черный", 150000.0, 10)
    category.add_product(new_product)

    assert len(category.products) == initial_product_count + 1
    assert Category.product_count == initial_product_count + 1
    assert new_product in category.products


def test_products_property(products):
    category = Category("Смартфоны", "Описание категории", products)
    assert category.products == products


def test_get_products(products):
    category = Category("Смартфоны", "Описание категории", products)
    products_list = category.get_products()

    assert len(products_list) == 3
    assert products_list[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert products_list[1] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert products_list[2] == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add_products(products):
    result1 = products[0] + products[1]
    result2 = products[1] + products[2]
    assert result1 == 2580000.0
    assert result2 == 2114000.0


def test_str_products(products):
    result1 = str(products[0])
    result2 = str(products[1])
    assert result1 == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert result2 == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_str_category(category):
    result1 = str(category)
    assert result1 == "Смартфоны, количество продуктов: 27 шт."


def test_sum_lawn_grass(grasses):
    result = grasses[0] + grasses[1]
    assert result == 16750.0


def test_sum_smartphones(smartphones):
    result = smartphones[0] + smartphones[1]
    assert result == 2580000.0


def test_invalid_sum_smartphones_and_grasses(smartphones, grasses):
    with pytest.raises(TypeError):
        smartphones[0] + grasses[0]

def test_mixin_log(capsys):
    Product("Телевизор", "Большой телевизор", 100000, 5)
    captured = capsys.readouterr()
    assert "Product(Телевизор, Большой телевизор, 100000, 5)" in captured.out