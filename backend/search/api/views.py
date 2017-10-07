import requests

from django.shortcuts import render
from django.conf import settings

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response


class EventsListAPIView(generics.ListAPIView):
    pass
