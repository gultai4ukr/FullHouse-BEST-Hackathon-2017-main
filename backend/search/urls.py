from django.conf.urls import url

from search.api.views import EventsListAPIView, EventGetAPIView

urlpatterns = [
    url(r'^events/$', EventsListAPIView.as_view()),
    url(r'^events/(?P<event_id>[a-zA-Z0-9\-]+)/$', EventGetAPIView.as_view()),
]