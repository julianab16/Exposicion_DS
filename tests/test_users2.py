import unittest
from apps.users.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class UserTestCase(unittest.TestCase):

    # def setUp(self):
    #     self.user_data = {
    #         "username": "usuario_test",
    #         "first_name": "Juan",
    #         "last_name": "Pérez",
    #         "email": "juanperez@example.com",
    #         "phone_number": 3104932234,
    #         "dni": 1107857432
    #     }

    # def test_create_valid_user(self):
    #     User = get_user_model()
    #     user = User.objects.create_user(**self.user_data)
    #     self.assertEqual(user.username, self.user_data["username"])
    #     self.assertEqual(user.email, self.user_data["email"].lower())
    #     self.assertIsNotNone(user.password)
        
# class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.user_data = User.objects.create_user(
            username="usuario_test",
            first_name=None,
            last_name= "Pérez",
            email= "juanperez@example.com",
            phone_number= 3104932234,
            dni= 1107857432,
            password = "contrasenhia"
        )

    def test_create_valid_user(self):
        # self.assertEqual(self.user_data.username,"usuario_test")
        self.assertEqual(self.user_data.email.lower(), self.user_data.email)
        self.assertEqual(self.user_data.password, "hello")
        #self.assertIsNotNone(self.user_data.first_name)