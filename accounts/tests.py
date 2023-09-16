from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse, resolve


@override_settings(
    SOCIALACCOUNT_PROVIDERS={
        "github": {
            "APP": {
                "client_id": "943fc152506a4b4fbce0",
                "secret": "043aaf95c123de948eced1cd6543efc87c2c1de5",
            }
        }
    }
)
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will", email="will@email.com", password="testpass123"
        )
        self.assertEquals(user.username, "will")
        self.assertEquals(user.email, "will@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEquals(admin_user.username, "superadmin")
        self.assertEquals(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_staff)


@override_settings(
    SOCIALACCOUNT_PROVIDERS={
        "github": {
            "APP": {
                "client_id": "943fc152506a4b4fbce0",
                "secret": "043aaf95c123de948eced1cd6543efc87c2c1de5",
            }
        }
    }
)
class SignUpPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
