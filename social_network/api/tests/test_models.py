from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserModelTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='bittu',
            password='syed@123'
        )
        self.assertEqual(user.email, 'syedajaz91@gmail.com')
        self.assertTrue(user.check_password('syed@123'))

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='syedajaz91@gmail.com',
            password='syed@123'
        )
        self.assertEqual(admin_user.email, 'syedajaz91@gmail.com')
        self.assertTrue(admin_user.is_superuser)
