from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test to create user with email and password"""
        email = "puneetrohtela@gmail.com"
        password = "puneet123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_email(self):
        """check user email is in lower case"""
        email = "puneet@GmAil.com"
        user = get_user_model().objects.create_user(email, "12432")
        self.assertEqual(user.email, email.lower())

    def test_raise_validation_error(self):
        """check email is not empty"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "12345")

    def test_check_super_user(self):
        """checking for super user """
        user = get_user_model().objects.create_superuser(
            "abc@gmail.com"
            "12345"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
