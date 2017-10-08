import requests

from backend import secrets

from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


class EventsListAPIView(views.APIView):

    BASE_URL = "http://api.eventful.com/json/events/search/"

    CATEGORIES = [
        'music', 'conference', 'comedy', 'learning_education', 'family_fun_kids',
        'festivals_parades', 'movies_film', 'food', 'fundraisers', 'art', 'support', 'holiday',
        'books', 'attractions', 'community', 'business', 'singles_social', 'schools_alumni',
        'clubs_associations', 'outdoors_recreation', 'performing_arts', 'animals',
        'politics_activism', 'sales', 'science', 'religion_spirituality', 'sports',
        'technology', 'other'
    ]

    DATA_KEYS = [
        'id', 'title', 'description', 'start_time', 'url', 'country_name', 'city_name'
    ]

    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Host": "api.qwant.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
    }

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
            r = response.json()
            events = []
            for e in r['events']['event']:
                data = {}
                for key in self.DATA_KEYS:
                    data[key] = e[key]
                res = requests.get(
                    "https://api.qwant.com/api/search/images?count=1&q={q}".format(q=data['title']),
                    headers=self.HEADERS
                )
                if res.ok:
                    data['image'] = res.json()['data']['result']['items'][0]['media']
                events.append(data)
            return Response(events)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EventGetAPIView(views.APIView):

    EVENTFUL_URL = "http://api.eventful.com/json/events/get/?app_key={app_key}".format(
        app_key=secrets.EVENTFUL_API_KEY,
    )
    AMADEUS_URL = "https://api.sandbox.amadeus.com/v1.2/hotels/search-circle/?apikey={api_key}".format(
        api_key=secrets.AMADEUS_CONSUMER_KEY
    )

    def get(self, request, *args, **kwargs):

        response = requests.get(
            "{url}&id={event_id}".format(
                url=self.EVENTFUL_URL, event_id=self.kwargs['event_id']
            )
        )

        if not response.ok:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        json = response.json()
        latitude = json['latitude']
        longitude = json['longitude']
        start_time = json['start_time']
        start_date = start_time and start_time.split(' ')[0]
        stop_time = json['stop_time']
        stop_date = stop_time and stop_time.split(' ')[0]

        data = {}

        if all([latitude, longitude, start_date, stop_date]):
            response = requests.get(
                "{url}&latitude={latitude}&longitude={longitude}"
                "&radius={radius}&check_in={check_in}&check_out={check_out}".format(
                    url=self.AMADEUS_URL, radius=10,
                    latitude=latitude, longitude=longitude,
                    check_in='2017-12-20', check_out='2017-12-27'
                )
            )

            if response.ok:
                results = response.json()['results']
                data['hotels'] = []
                for r in results:
                    hotel_data = dict(
                        name=r['property_name'],
                        address=r['address'],
                        price=r['total_price'],
                        contacts=r['contacts'],
                        images=r['images']
                    )
                    data['hotels'].append(hotel_data)

        return Response(data)
