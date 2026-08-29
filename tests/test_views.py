from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(
            title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(
            title="Pizza", price=120, inventory=50)
        self.item3 = MenuItem.objects.create(
            title="Pasta", price=95, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')

        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
