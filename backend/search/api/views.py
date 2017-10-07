import requests
import xml.etree.ElementTree as ET
from backend import secrets

from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


class EventsGetAPIView(views.APIView):

    BASE_URL = "http://api.eventful.com/rest/events/search/"

    CATEGORIES = [
        'music', 'conference', 'comedy', 'learning_education', 'family_fun_kids',
        'festivals_parades', 'movies_film', 'food', 'fundraisers', 'art', 'support', 'holiday',
        'books', 'attractions', 'community', 'business', 'singles_social', 'schools_alumni',
        'clubs_associations', 'outdoors_recreation', 'performing_arts', 'animals',
        'politics_activism', 'sales', 'science', 'religion_spirituality', 'sports',
        'technology', 'other'
    ]

    DATA_KEYS = [
        'title', 'description', 'start_time', 'url', 'country_name', 'city_name', 'image'
    ]

    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category', "")
        location = request.query_params.get('location', "")
        keywords = request.query_params.get('keywords', "")
        from_date = request.query_params.get('from_date', "20000101")
        to_date = request.query_params.get('to_date', "21000101")
        page_number = request.query_params.get('page_number', "")

        if category and category not in self.CATEGORIES:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = requests.get(
            "{base_url}?app_key={app_key}&category={category}&location={location}&"
            "keywords={keywords}&date='{from_date}00-{to_date}00'&page_number={page_number}".format(
                base_url=self.BASE_URL, category=category, location=location,
                keywords=keywords, app_key=secrets.EVENTFUL_API_KEY,
                from_date=from_date, to_date=to_date, page_number=page_number
            )
        )

        if response.ok:
            root = ET.fromstring(response.content)
            events = []
            for r in root.iter('event'):
                data = {}
                for key in self.DATA_KEYS:
                    data[key] = r.find(key).text
                events.append(data)
            return Response(events)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
