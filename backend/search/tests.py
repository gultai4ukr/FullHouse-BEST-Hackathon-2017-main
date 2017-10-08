from rest_framework import status
from rest_framework.test import APITestCase


class EventsListAPITest(APITestCase):

    def test_get_events_by_category(self):

        response = self.client.get(
            '/search/events/?category=music'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(set(response.data[0].keys()), {
            'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
        })

    def test_get_events_by_keywords(self):

        response = self.client.get(
            '/search/events/?keywords=film'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(set(response.data[0].keys()), {
            'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
        })

    def test_get_events_by_location(self):

        response = self.client.get(
            '/search/events/?location=Ukraine'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(set(response.data[0].keys()), {
            'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
        })

    def test_get_events_by_date(self):

        response = self.client.get(
            '/search/events/?from_date=20170909&to_date=20170913'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(set(response.data[0].keys()), {
            'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
        })

    def test_get_events_with_pagination(self):

        response = self.client.get(
            '/search/events/?location=Ukraine&page_number=2'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(set(response.data[0].keys()), {
            'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
        })

    def test_get_events_without_params(self):

        response = self.client.get(
            '/search/events/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(set(response.data[0].keys()), {
            'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
        })

    def test_get_events_with_incorrect_category(self):

        response = self.client.get(
            '/search/events/?category=olololo'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EventGetAPITest(APITestCase):

    def test_get_events_by_category(self):

        response = self.client.get(
            '/search/events/E0-001-000278174-6/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})
