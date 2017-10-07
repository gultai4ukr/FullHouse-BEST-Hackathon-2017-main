from django.conf.urls import url

from search.api.views import EventsGetAPIView

urlpatterns = [
    url(r'^events/$', EventsGetAPIView.as_view())
]