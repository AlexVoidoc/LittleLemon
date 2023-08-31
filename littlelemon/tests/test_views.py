from django.test import TestCase
from restaurant import views, models, serializers

class MenuViewTest(TestCase):
    def setUp(self):
        models.Menu.objects.create(id=3, title="IceCream", price=80, inventory=100)
        models.Menu.objects.create(id=4, title="Chocolate", price=40, inventory=120)
        models.Menu.objects.create(id=5, title="Cake", price=200, inventory=60)

    def test_getall(self):
        items = models.Menu.objects.all()
        serializer = serializers.MenuSerializer(items, many=True)
        serialized_data = serializer.data

        correct_data = [
            {"id": 3, "title": "IceCream", "price": '80.00', "inventory": 100},
            {"id": 4, "title": "Chocolate", "price": '40.00', "inventory": 120},
            {"id": 5, "title": "Cake", "price": '200.00', "inventory": 60},
        ]

        serialized_data_dicts = [{key: value for key, value in item.items()} for item in serialized_data]

        self.assertEqual(serialized_data_dicts, correct_data)