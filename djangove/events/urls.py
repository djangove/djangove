# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers

from djangove.events.api import SpeakerViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'speaker', SpeakerViewSet)

urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-app/', include(router.urls)),
]
