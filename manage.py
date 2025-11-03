from rest_framework.test import APITestCase
from home.models import Restaurant

class RestaurantInfoAPITest(APITestCase):
    def test_get_restaurant_info(self):
        restaurant=Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St"
        )
        response=self.client.get('/api/restaurant-info')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], restaurant.name)
        self.assertEqual(response.data['address'], restaurant.address)
        
        
         
