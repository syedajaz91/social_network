from django.test import TestCase
from api.serializers import UserSerializer
from django.contrib.auth import get_user_model

class UserSerializerTests(TestCase):

    def test_valid_user_serializer(self):
        User = get_user_model()
        user = User.objects.create_user(email='testuser@example.com', password='password123')
        serializer = UserSerializer(instance=user)
        data = serializer.data
        self.assertEqual(set(data.keys()), {'id', 'email'})

    def test_invalid_user_serializer(self):
        invalid_data = {'email': 'invalid', 'password': 'short'}
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
