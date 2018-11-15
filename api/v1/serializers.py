from rest_framework import serializers



class FaviconSerializer(serializers.Serializer):

    url = serializers.URLField()
    extension = serializers.CharField()
    size = serializers.IntegerField()
