from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework      import status

from products.models import Product


class ProductTestCase(APITestCase):
    def setUp(self):
        user = get_user_model()
        self.test_user_01 = user.objects.create_user(username="test_user_01", password="password")
        self.test_user_02 = user.objects.create_user(username="test_user_02", password="password")
        self.test_user_03 = user.objects.create_user(username="test_user_03", password="password")
        self.test_user_04 = user.objects.create_user(username="test_user_04", password="password")
        self.test_user_05 = user.objects.create_user(username="test_user_05", password="password")

    def test_products(self):
        data_01 = {
            "title" : "test_바디크림",
            "publisher" : self.test_user_01.id,
            "one_price" : 10000,
            "amount" : 1000000,
            "end_date" : datetime.now() + timedelta(days=30),
            "description" : "test_description"
        }

        response = self.client.post('/products/', data=data_01, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        data_02 = {
            "title" : "test_의자",
            "publisher" : self.test_user_02.id,
            "one_price" : 20000,
            "amount" : 3000000,
            "end_date" : datetime.now() + timedelta(days=20),
            "description" : "test_description"
        }

        response = self.client.post('/products/', data=data_02, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

        # 필수 데이터가 부족한 경우 에러 시작
        data_non_amount = {
            "title" : "test_침대",
            "publisher" : self.test_user_02.id,
            "one_price" : 20000,
            "end_date" : datetime.now() + timedelta(days=20),
            "description" : "test_description"
        }

        response = self.client.post('/products/', data=data_non_amount, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data_non_one_price = {
            "title" : "test_책상",
            "publisher" : self.test_user_02.id,
            "amount" : 3000000,
            "end_date" : datetime.now() + timedelta(days=20),
            "description" : "test_description"
        }

        response = self.client.post('/products/', data=data_non_one_price, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data_non_publisher = {
            "title" : "test_노트북",
            "one_price" : 20000,
            "amount" : 3000000,
            "end_date" : datetime.now() + timedelta(days=20),
            "description" : "test_description"
        }

        response = self.client.post('/products/', data=data_non_publisher, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data_non_end_date = {
            "title" : "test_맥북",
            "publisher" : self.test_user_02.id,
            "one_price" : 20000,
            "amount" : 3000000,
            "description" : "test_description"
        }

        response = self.client.post('/products/', data=data_non_end_date, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # 필수 데이터가 부족한 경우 에러 종료

        # Detail View 시작
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['d_day'], 29)

        data_patch_amount = {"amount" : 2000000}
        response = self.client.patch('/products/1', data_patch_amount)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=1).amount, 1000000)
        
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
        # Detail View 종료


