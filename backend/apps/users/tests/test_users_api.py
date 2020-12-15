import json

from datetime import datetime, timedelta
from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework import status
from apps.users.models import User, UserManager


# Create your tests here.
class TestUserAPIViewSet(APITestCase):

    def setUp(self):
        # Create User
        self.user = User()
        self.user.username = "hjhong"
        self.user.email = "hj.hong@haezoom.com"
        self.user.is_staff = 1
        self.user.is_superuser = 1
        self.user.set_password("testpwd")
        self.user.date_of_birth = timezone.now()
        self.user.date_joined = timezone.now()
        self.user.save()

        # Remove authenticate step
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        User.objects.all().delete()

    def _create(self, data, status_code):
        response = self.client.post(
            "/api/blog/",
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status_code)

    def test_create(self):
        pass
        # self._create(
        #     {
        #         "plant_id": self.plant.id,
        #         "start_date": "2020-11-01",
        #         "end_date": "2020-11-30",
        #         "electric_rate": 100,
        #         "saving_coast": 200,
        #     },
        #     status.HTTP_200_OK,
        # )
    def test_create_fail(self):
         pass
            # self._create(
            #     {
            #         "start_date": "2020-11-01",
            #         "end_date": "2020-11-30",
            #         "electric_rate": 100,
            #         "saving_coast": 200,
            #     },
            #     status.HTTP_400_BAD_REQUEST,
            # )        

    def test_get(self):
        response = self.client.get(f"/api/users/{self.user.id}")
        result = response.json()["result"]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.email, result["email"])
        self.assertEqual(self.user.username, result["username"])

    

        

            
        