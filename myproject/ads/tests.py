from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Ad, ExchangeProposal


class AdCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob", password="qwerty")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_create_ad(self):
        response = self.client.post(
            reverse("ads:ad_create"),
            {
                "title": "Smartphone Samsung",
                "description": "some description",
                "user": "1",
                "category": "Smartphones",
                "condition": "New",
            }
        )
        self.assertRedirects(response, reverse("ads:ads_list"))


class AdViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob", password="qwerty")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.ad = Ad.objects.create(
            title="Smartphone Samsung",
            description="some description",
            user=self.user,
            category="Smartphones",
            condition="New",
        )

    def tearDown(self) -> None:
        self.ad.delete()

    def test_update_ad(self):
        response = self.client.post(
            reverse("ads:ad_update", kwargs={"pk": self.ad.pk}),
            {"title": "Smartphone Samsung Galaxy 128 Gb"}
        )
        self.assertRedirects(response, reverse("ads:ads_list"))

    def test_list_ads(self):
        response = self.client.get(reverse("ads:ads_list"))
        self.assertContains(response, self.ad.title)
        self.assertContains(response, self.ad.description)

    def test_delete_ad(self):
        response = self.client.post(
            reverse("ads:ad_delete", kwargs={"pk": self.ad.pk})
        )
        self.assertRedirects(response, reverse("ads:ads_list"))

        response_list = self.client.get(reverse("ads:ads_list"))
        self.assertContains(response_list, "No ads yet")

    def test_search_ad(self):
        response = self.client.get(
            "http://127.0.0.1:8000/ads/api/ads/?search=smartphone"
        )
        self.assertEqual(response.data["count"], 1)

    def test_filter_ad(self):
        response = self.client.get(
            "http://127.0.0.1:8000/ads/api/ads/?category=&condition=New"
        )
        self.assertEqual(response.data["count"], 1)


class ExchangeViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username="bob", password="qwerty")
        cls.user_2 = User.objects.create_user(username="tom", password="abcdef")

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.user_2.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user_1)
        self.ad_1 = Ad.objects.create(
            title="Smartphone Samsung",
            description="some description",
            user=self.user_1,
            category="Smartphones",
            condition="New",
        )
        self.client.force_login(self.user_2)
        self.ad_2 = Ad.objects.create(
            title="Laptop Lenovo",
            description="Laptop for everyday work",
            user=self.user_2,
            category="Laptops",
            condition="Used",
        )

    def test_create_exchange_proposal(self):
        response = self.client.post(
            reverse("ads:exchange_create"),
            {
                "ad_sender": "1",
                "ad_receiver": "2",
                "comment": "Hello. Would you like to exchange?",
            }
        )
        self.assertRedirects(response, reverse("ads:exchanges_list"))

    def test_update_exchange_proposal(self):
        self.exchange = ExchangeProposal.objects.create(
                ad_sender=self.ad_1,
                ad_receiver=self.ad_2,
                comment="Hello. Would you like to exchange?",
        )
        response = self.client.post(
            reverse("ads:exchange_update", kwargs={"pk": self.exchange.pk}),
            {"status": "принята"}
        )
        self.assertRedirects(response, reverse("ads:exchanges_list"))
