# -*- coding: utf-8 -*-

from rest_framework import serializers, viewsets

from djangove.events.models import EventPageSpeaker


class SpeakerSerializerList(serializers.ModelSerializer):

    class Meta:
        model = EventPageSpeaker


class SpeakerViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = EventPageSpeaker.objects.all()
    serializer_class = SpeakerSerializerList
