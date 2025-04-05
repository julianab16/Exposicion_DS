# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from apps.products.models import Product 

# class ProductModelTest(TestCase):

#     def setUp(self):
#         self.product_data = Product.objects.create(
#             name="Pastel de chocolate",
#             description="Delicioso pastel de chocolate",
#             price=14.990,
#             available=True,
#             photo=None
#         )
    
#     def test_create_valid_product(self):
#         self.assertEqual(self.product_data.name, "Pastel de chocolate")
#         self.assertEqual(self.product_data.description, "Delicioso pastel de chocolate")
#         self.assertEqual(self.product_data.price, 14.990)
#         self.assertTrue(self.product_data.available)

#     # def test_negative_price(self):
#     #     product = Product(
#     #         name="Azucar",
#     #         description="Azucar de caña",
#     #         price=-5000, #Precio negativo
#     #         available=True
#     #     )
#     #     with self.assertRaises(ValidationError):
#     #         product.full_clean()

#     # def test_long_description(self):
#     #     product = Product(
#     #         name="Pan",
#     #         description="a" * 301,  # Límite es 300
#     #         price=3.000,
#     #         available=True
#     #     )
#     #     with self.assertRaises(ValidationError):
#     #         product.full_clean()
    
#     def test_create_another_valid_product(self):
#         self.another_product_data = Product.objects.create(
#             name="Milo",
#             description="Delicioso Milo con leche",
#             price=4.990,
#             available=True,
#             photo=None
#         )
#         self.assertEqual(self.another_product_data.name, "Milo")
#         self.assertEqual(self.another_product_data.description, "Delicioso Milo con leche")
#         self.assertEqual(self.another_product_data.price, 4.0) 
#         self.assertTrue(self.another_product_data.available)

