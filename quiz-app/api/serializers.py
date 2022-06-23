from rest_framework import serializers

from base import models


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = '__all__'
