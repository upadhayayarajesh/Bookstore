from allauth.socialaccount.models import SocialApp
from django.test import TestCase, override_settings
from django.urls import reverse, resolve

from pages.views import HomePageView, AboutPageView


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
class HomePageTest(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEquals(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertEquals(self.response.status_code, 200)

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEquals(view.func.__name__, HomePageView.as_view().__name__)


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
class AboutPagesTests(TestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
