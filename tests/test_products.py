from django.test import TestCase
from apps.products.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        """Crea un producto antes de cada prueba"""
        self.product = Product.objects.create(
            name="Capuchino",
            description="Café con espuma de leche",
            price=4.50,
            available=True,
        )

    def test_product_creation(self):
        print("hola putos")
        """Verifica que el producto se creó correctamente"""
        self.assertEqual(self.product.name, "Capuchino")
        self.assertEqual(self.product.price, 4.50)
        self.assertTrue(self.product.available)