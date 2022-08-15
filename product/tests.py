from django.test import TestCase, Client

# Create your tests here.


class TestProduct(TestCase):

    def mytest(self):
        my_client = Client()
        response = my_client.get("http://localhost:8000/buy/")
        assert response.status_code == 200
