from rest_framework import serializers
from .models import Song, Artist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id','title','imageUrl','lyrics','artist')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['artist'] = ArtistSerializer(instance.artist).data
        return data

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True,read_only=True)
    class Meta:
        model = Artist
        fields = ('id','name','imageUrl','songs')
    
