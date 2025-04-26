import unittest
from src.utils import Product, Category


class TestProductAndCategory(unittest.TestCase):

    def setUp(self):
        # Обнуляем счётчики перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

    def test_product_creation(self):
        product = Product("Test Phone", "Description", 999.99, 3)
        self.assertEqual(product.name, "Test Phone")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.quantity, 3)

    def test_category_creation(self):
        p1 = Product("Phone", "Desc", 100.0, 2)
        p2 = Product("Tablet", "Desc", 200.0, 1)
        category = Category("Gadgets", "Various gadgets", [p1, p2])

        self.assertEqual(category.name, "Gadgets")
        self.assertEqual(category.description, "Various gadgets")
        self.assertEqual(len(category.products), 2)
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 2)

    def test_multiple_categories(self):
        products1 = [Product("P1", "D1", 1.0, 1), Product("P2", "D2", 2.0, 2)]
        products2 = [Product("P3", "D3", 3.0, 3)]
        Category("Category1", "Desc1", products1)
        Category("Category2", "Desc2", products2)

        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.product_count, 3)


if __name__ == "__main__":
    unittest.main()
