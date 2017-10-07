from django.conf.urls import url

from search.api.views import EventsListAPIView

urlpatterns = [
    url(r'^events/$', EventsListAPIView.as_view())
]