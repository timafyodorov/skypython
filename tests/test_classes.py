import pytest

from src.classes import BaseProduct, Category, LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def sample_category(sample_product):
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций "
            "для удобства жизни"
        ),
        products=[sample_product],
    )


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


def test_product_initialization(sample_product):
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Invalid Product", "Test desc", 1000.0, 0)


def test_category_initialization(sample_category):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций "
        "для удобства жизни"
    )
    assert len(sample_category._Category__products) == 1
    assert isinstance(sample_category._Category__products[0], Product)


def test_category_count():
    Category.category_count = 0
    category1 = Category("Books", "Printed books", [])
    assert Category.category_count == 1
    assert category1.name == "Books"
    category2 = Category("Toys", "Children toys", [])
    assert Category.category_count == 2
    assert category2.name == "Toys"


def test_product_count(sample_product):
    Category.product_count = 0
    category = Category(
        "Electronics", "Electronic devices", [sample_product, sample_product]
    )
    assert Category.product_count == 2
    assert len(category._Category__products) == 2


def test_empty_category():
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Empty", "No products", [])
    assert len(category._Category__products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(sample_product):
    Category.product_count = 0
    category = Category("Test", "Test category", [])
    category.add_product(sample_product)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1
    assert category._Category__products[0] == sample_product
    with pytest.raises(TypeError):
        category.add_product("not a product")


def test_add_product_subclass(sample_smartphone, sample_lawn_grass):
    category = Category("Test", "Test category", [])
    Category.product_count = 0
    category.add_product(sample_smartphone)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1
    assert isinstance(category._Category__products[0], Product)
    assert isinstance(category._Category__products[0], Smartphone)
    category.add_product(sample_lawn_grass)
    assert len(category._Category__products) == 2
    assert Category.product_count == 2
    assert isinstance(category._Category__products[1], LawnGrass)


def test_products_getter(sample_product):
    category = Category("Test", "Test category", [sample_product])
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test description",
        "price": 1000.0,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 1000.0
    assert product.quantity == 10


def test_price_getter_setter(sample_product):
    assert sample_product.price == 180000.0
    sample_product.price = 200000.0
    assert sample_product.price == 200000.0
    sample_product.price = 0
    assert sample_product.price == 200000.0
    sample_product.price = -100
    assert sample_product.price == 200000.0


def test_product_str(sample_product):
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(sample_product) == expected


def test_category_str(sample_product):
    category = Category("Test", "Test category", [sample_product])
    expected = "Test, количество продуктов: 5 шт."
    assert str(category) == expected


def test_smartphone_initialization(sample_smartphone):
    assert sample_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "S23 Ultra"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Серый"


def test_lawn_grass_initialization(sample_lawn_grass):
    assert sample_lawn_grass.name == "Газонная трава"
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "7 дней"
    assert sample_lawn_grass.color == "Зеленый"


def test_add_method(sample_smartphone, sample_lawn_grass, sample_product):
    smartphone2 = Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    lawn_grass2 = LawnGrass(
        name="Premium Grass",
        description="Premium lawn grass",
        price=600.0,
        quantity=15,
        country="USA",
        germination_period="5 дней",
        color="Green",
    )
    product2 = Product(
        name="Test Product", description="Test desc", price=1000.0, quantity=10
    )
    assert sample_smartphone + smartphone2 == 2580000.0  # 180000*5 + 210000*8
    assert sample_lawn_grass + lawn_grass2 == 19000.0  # 500*20 + 600*15
    assert sample_product + product2 == 910000.0  # 180000*5 + 1000*10
    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        sample_smartphone + "not a product"
    with pytest.raises(
        TypeError, match="Можно складывать только объекты одного класса"
    ):
        sample_smartphone + sample_lawn_grass
    with pytest.raises(
        TypeError, match="Можно складывать только объекты одного класса"
    ):
        sample_smartphone + sample_product
    with pytest.raises(
        TypeError, match="Можно складывать только объекты одного класса"
    ):
        sample_product + sample_smartphone
    with pytest.raises(
        TypeError, match="Можно складывать только объекты одного класса"
    ):
        sample_lawn_grass + sample_product
    with pytest.raises(
        TypeError, match="Можно складывать только объекты одного класса"
    ):
        sample_product + sample_lawn_grass


def test_print_init_mixin(capsys):
    Product(name="Test Product", description="Test desc", price=1000.0, quantity=10)
    captured = capsys.readouterr()
    assert captured.out.startswith(
        "Создан объект Product('Test Product', 'Test desc', 1000.0, 10)"
    )

    Smartphone(
        name="Test Smartphone",
        description="Test desc",
        price=2000.0,
        quantity=5,
        efficiency=90.0,
        model="Test Model",
        memory=128,
        color="Black",
    )
    captured = capsys.readouterr()
    assert captured.out.startswith(
        "Создан объект Smartphone('Test Smartphone', 'Test desc', 2000.0, 5)"
    )


def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct()


def test_category_middle_price(sample_product):
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Test", "Test category", [sample_product, product2])
    expected_middle_price = (180000.0 + 210000.0) / 2  # 195000.0
    assert category.middle_price() == expected_middle_price


def test_category_middle_price_empty():
    category = Category("Empty", "No products", [])
    assert category.middle_price() == 0


def test_product_zero_quantity_smartphone():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Smartphone(
            name="Invalid Smartphone",
            description="Test desc",
            price=2000.0,
            quantity=0,
            efficiency=90.0,
            model="Test Model",
            memory=128,
            color="Black",
        )


def test_product_zero_quantity_lawn_grass():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        LawnGrass(
            name="Invalid Grass",
            description="Test desc",
            price=500.0,
            quantity=0,
            country="Россия",
            germination_period="7 дней",
            color="Зеленый",
        )


def test_smartphone_init_additional():
    smartphone = Smartphone(
        name="Test Phone",
        description="Test desc",
        price=1500.0,
        quantity=3,
        efficiency=85.0,
        model="Test Model",
        memory=64,
        color="Blue",
    )
    assert smartphone.efficiency == 85.0
    assert smartphone.model == "Test Model"
    assert smartphone.memory == 64
    assert smartphone.color == "Blue"


def test_lawn_grass_init_additional():
    lawn_grass = LawnGrass(
        name="Test Grass",
        description="Test desc",
        price=300.0,
        quantity=10,
        country="USA",
        germination_period="10 дней",
        color="Dark Green",
    )
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "10 дней"
    assert lawn_grass.color == "Dark Green"


def test_smartphone_init_edge_cases():
    smartphone = Smartphone(
        name="Edge Phone",
        description="Edge case",
        price=0.01,
        quantity=1,
        efficiency=0.0,
        model="Edge",
        memory=1,
        color="",
    )
    assert smartphone.efficiency == 0.0
    assert smartphone.model == "Edge"
    assert smartphone.memory == 1
    assert smartphone.color == ""


def test_lawn_grass_init_edge_cases():
    lawn_grass = LawnGrass(
        name="Edge Grass",
        description="Edge case",
        price=0.01,
        quantity=1,
        country="",
        germination_period="",
        color="",
    )
    assert lawn_grass.country == ""
    assert lawn_grass.germination_period == ""
    assert lawn_grass.color == ""