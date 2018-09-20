from rest_framework import serializers, viewsets
from .models import Song


class SongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artist')


class SongsViewSet(viewsets.ModelViewSet):
    serializer_class = SongsSerializer
    queryset = Song.objects.all()
