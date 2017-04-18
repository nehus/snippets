from rest_framework import serializers
from snippets.models import *
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'name', 'description')